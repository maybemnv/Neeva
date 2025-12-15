from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.api import deps
from app.models import MoodLog, User
from app.schemas import MoodLog as MoodLogSchema, MoodLogCreate, MoodStats
from datetime import datetime, timedelta

router = APIRouter()

@router.post("/", response_model=MoodLogSchema)
def create_mood_log(
    *,
    db: Session = Depends(deps.get_db),
    mood_in: MoodLogCreate,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    mood_log = MoodLog(
        mood_level=mood_in.mood_level,
        notes=mood_in.notes,
        user_id=current_user.id,
    )
    db.add(mood_log)
    db.commit()
    db.refresh(mood_log)
    return mood_log

@router.get("/", response_model=List[MoodLogSchema])
def read_mood_logs(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    mood_logs = (
        db.query(MoodLog)
        .filter(MoodLog.user_id == current_user.id)
        .order_by(MoodLog.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    return mood_logs

@router.get("/stats", response_model=MoodStats)
def get_mood_stats(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    # Total entries
    total_entries = db.query(MoodLog).filter(MoodLog.user_id == current_user.id).count()
    
    # Average mood
    avg_mood = db.query(func.avg(MoodLog.mood_level)).filter(MoodLog.user_id == current_user.id).scalar() or 0
    
    # Weekly trend (last 7 days)
    today = datetime.utcnow().date()
    week_ago = today - timedelta(days=6)
    weekly_logs = (
        db.query(MoodLog)
        .filter(MoodLog.user_id == current_user.id, MoodLog.created_at >= week_ago)
        .all()
    )
    # Simplified trend logic
    weekly_trend = [0] * 7 # Placeholder
    
    # Mood distribution
    distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    all_logs = db.query(MoodLog).filter(MoodLog.user_id == current_user.id).all()
    for log in all_logs:
        if log.mood_level in distribution:
            distribution[log.mood_level] += 1
            
    return {
        "total_entries": total_entries,
        "average_mood": round(avg_mood, 1),
        "streak": 0, # Implement streak logic later
        "weekly_trend": weekly_trend,
        "mood_distribution": distribution
    }
