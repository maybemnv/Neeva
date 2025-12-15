from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime

class MoodLogBase(BaseModel):
    mood_level: int
    notes: Optional[str] = None

class MoodLogCreate(MoodLogBase):
    pass

class MoodLog(MoodLogBase):
    id: int
    user_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class MoodStats(BaseModel):
    total_entries: int
    average_mood: float
    streak: int
    weekly_trend: List[int]
    mood_distribution: dict
