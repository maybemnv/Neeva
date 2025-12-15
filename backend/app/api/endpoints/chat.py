from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.models import ChatMessage, User
from app.schemas import ChatMessage as ChatMessageSchema, ChatRequest
from app.services import ai
import traceback

router = APIRouter()

@router.post("/", response_model=ChatMessageSchema)
def chat_with_neeva(
    *,
    db: Session = Depends(deps.get_db),
    chat_request: ChatRequest,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    try:
        # 1. Save user message
        user_msg = ChatMessage(
            user_id=current_user.id,
            role="user",
            content=chat_request.message
        )
        db.add(user_msg)
        db.commit()
        
        # 2. Get conversation history (last 10 messages)
        history = (
            db.query(ChatMessage)
            .filter(ChatMessage.user_id == current_user.id)
            .order_by(ChatMessage.created_at.desc())
            .limit(10)
            .all()
        )
        history.reverse() # Oldest first
        
        formatted_history = [{"role": msg.role, "content": msg.content} for msg in history]
        
        # 3. Get user's onboarding data for personalization
        user_context = current_user.onboarding_data or {}
        
        # 4. Generate AI response with personalization
        ai_response_text = ai.get_chat_response(formatted_history, user_context)
        
        # 5. Save AI response
        ai_msg = ChatMessage(
            user_id=current_user.id,
            role="assistant",
            content=ai_response_text
        )
        db.add(ai_msg)
        db.commit()
        db.refresh(ai_msg)
        
        # Return as dict to avoid ORM issues
        return {
            "id": ai_msg.id,
            "user_id": ai_msg.user_id,
            "role": ai_msg.role,
            "content": ai_msg.content,
            "created_at": ai_msg.created_at
        }
    except Exception as e:
        print(f"Chat endpoint error: {e}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history", response_model=List[ChatMessageSchema])
def get_chat_history(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 50,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    messages = (
        db.query(ChatMessage)
        .filter(ChatMessage.user_id == current_user.id)
        .order_by(ChatMessage.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    return messages
