from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas import User as UserSchema
from app.models import User # Assuming User model is in app.models

router = APIRouter()

@router.get("/me", response_model=UserSchema)
def read_user_me(
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    return current_user

@router.post("/onboarding", response_model=UserSchema)
def update_onboarding(
    data: dict,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    current_user.onboarding_data = data
    current_user.onboarding_completed = True
    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user
