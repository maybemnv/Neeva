from fastapi import APIRouter
from app.api.endpoints import auth, users, mood, chat, exercises, community

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(mood.router, prefix="/mood", tags=["mood"])
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
api_router.include_router(exercises.router, prefix="/exercises", tags=["exercises"])
api_router.include_router(community.router, prefix="/community", tags=["community"])
