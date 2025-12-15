from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime

class CommunityGroupBase(BaseModel):
    name: str
    description: str

class CommunityGroup(CommunityGroupBase):
    id: int
    member_count: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommunityPostBase(BaseModel):
    content: str
    is_anonymous: bool = False
    group_id: int

class CommunityPostCreate(CommunityPostBase):
    pass

class CommunityPost(CommunityPostBase):
    id: int
    user_id: int
    likes_count: int
    comment_count: int
    created_at: datetime
    # We might want to return user name if not anonymous, but keep simple for now

    model_config = ConfigDict(from_attributes=True)
