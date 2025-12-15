from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.models import CommunityPost, CommunityGroup, User
from app.schemas import CommunityPost as PostSchema, CommunityPostCreate, CommunityGroup as GroupSchema

router = APIRouter()

@router.get("/groups", response_model=List[GroupSchema])
def get_groups(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    groups = db.query(CommunityGroup).offset(skip).limit(limit).all()
    return groups

@router.post("/groups", response_model=GroupSchema)
def create_group(
    *,
    db: Session = Depends(deps.get_db),
    name: str,
    description: str,
    current_user: User = Depends(deps.get_current_user), # Only admin should do this ideally
) -> Any:
    group = CommunityGroup(name=name, description=description)
    db.add(group)
    db.commit()
    db.refresh(group)
    return group

@router.post("/posts", response_model=PostSchema)
def create_post(
    *,
    db: Session = Depends(deps.get_db),
    post_in: CommunityPostCreate,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    post = CommunityPost(
        content=post_in.content,
        is_anonymous=post_in.is_anonymous,
        group_id=post_in.group_id,
        user_id=current_user.id,
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@router.get("/posts", response_model=List[PostSchema])
def get_posts(
    db: Session = Depends(deps.get_db),
    group_id: int = None,
    skip: int = 0,
    limit: int = 50,
) -> Any:
    query = db.query(CommunityPost)
    if group_id:
        query = query.filter(CommunityPost.group_id == group_id)
    
    posts = query.order_by(CommunityPost.created_at.desc()).offset(skip).limit(limit).all()
    return posts
