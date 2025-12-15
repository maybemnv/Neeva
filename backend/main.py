from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.middleware.error_logging import ErrorLoggingMiddleware

app = FastAPI(title="Neeva API", description="AI Mental Wellness Companion API")

# Add error logging middleware FIRST
app.add_middleware(ErrorLoggingMiddleware)

# CORS Configuration - Allow all origins for now (configure specific origins for production security)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.api.api import api_router

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to Neeva API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
