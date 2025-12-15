from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.api import deps
from app.models import ExerciseCompleted, User
from app.schemas import ExerciseCompleted as ExerciseSchema, ExerciseCompletedCreate, ExerciseStats

router = APIRouter()

@router.post("/", response_model=ExerciseSchema)
def complete_exercise(
    *,
    db: Session = Depends(deps.get_db),
    exercise_in: ExerciseCompletedCreate,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    exercise = ExerciseCompleted(
        exercise_id=exercise_in.exercise_id,
        duration_completed=exercise_in.duration_completed,
        user_id=current_user.id,
    )
    db.add(exercise)
    db.commit()
    db.refresh(exercise)
    return exercise

@router.get("/stats", response_model=ExerciseStats)
def get_exercise_stats(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    total_seconds = db.query(func.sum(ExerciseCompleted.duration_completed)).filter(ExerciseCompleted.user_id == current_user.id).scalar() or 0
    total_minutes = int(total_seconds / 60)
    
    sessions_completed = db.query(ExerciseCompleted).filter(ExerciseCompleted.user_id == current_user.id).count()
    
    return {
        "total_minutes": total_minutes,
        "sessions_completed": sessions_completed,
        "streak": 0 # Implement streak logic later
    }

@router.get("/history", response_model=List[ExerciseSchema])
def get_exercise_history(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 50,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    exercises = (
        db.query(ExerciseCompleted)
        .filter(ExerciseCompleted.user_id == current_user.id)
        .order_by(ExerciseCompleted.completed_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    return exercises
