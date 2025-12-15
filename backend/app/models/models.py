from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    name = Column(String)
    timezone = Column(String, default="UTC")
    onboarding_completed = Column(Boolean, default=False)
    onboarding_data = Column(JSON, default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    mood_logs = relationship("MoodLog", back_populates="user")
    chat_messages = relationship("ChatMessage", back_populates="user")
    exercises_completed = relationship("ExerciseCompleted", back_populates="user")
    community_posts = relationship("CommunityPost", back_populates="user")
    preferences = relationship("UserPreference", uselist=False, back_populates="user")

class MoodLog(Base):
    __tablename__ = "mood_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    mood_level = Column(Integer)  # 1-5
    notes = Column(Text)  # Encrypted
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="mood_logs")

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    role = Column(String)  # user/assistant
    content = Column(Text)  # Encrypted
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="chat_messages")

class ExerciseCompleted(Base):
    __tablename__ = "exercises_completed"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    exercise_id = Column(String)
    duration_completed = Column(Integer)  # Seconds
    completed_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="exercises_completed")

class CommunityGroup(Base):
    __tablename__ = "community_groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    member_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    posts = relationship("CommunityPost", back_populates="group")

class CommunityPost(Base):
    __tablename__ = "community_posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    group_id = Column(Integer, ForeignKey("community_groups.id"))
    content = Column(Text)
    is_anonymous = Column(Boolean, default=False)
    likes_count = Column(Integer, default=0)
    comment_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="community_posts")
    group = relationship("CommunityGroup", back_populates="posts")

class UserPreference(Base):
    __tablename__ = "user_preferences"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    notifications = Column(JSON)
    theme = Column(String, default="auto")
    language = Column(String, default="en")
    privacy_settings = Column(JSON)

    user = relationship("User", back_populates="preferences")
