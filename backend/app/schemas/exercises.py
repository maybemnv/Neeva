from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime

class ExerciseCompletedBase(BaseModel):
    exercise_id: str
    duration_completed: int

class ExerciseCompletedCreate(ExerciseCompletedBase):
    pass

class ExerciseCompleted(ExerciseCompletedBase):
    id: int
    user_id: int
    completed_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExerciseStats(BaseModel):
    total_minutes: int
    sessions_completed: int
    streak: int
