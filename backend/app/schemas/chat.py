from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime

class ChatMessageBase(BaseModel):
    role: str
    content: str

class ChatMessageCreate(ChatMessageBase):
    pass

class ChatMessage(ChatMessageBase):
    id: int
    user_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ChatRequest(BaseModel):
    message: str
