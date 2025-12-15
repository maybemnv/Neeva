from datetime import timedelta
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core import security
from app.core.database import get_db
from app.models import User
from app.schemas import Token, UserCreate, User as UserSchema

router = APIRouter()

@router.get("/test")
def test_endpoint():
    return {"message": "Auth router is working"}

@router.post("/login", response_model=Token)
def login_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        user.email, expires_delta=access_token_expires
    )
    refresh_token = security.create_refresh_token(user.email)
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "refresh_token": refresh_token
    }

@router.post("/register", response_model=UserSchema)
def register_user(
    *,
    db: Session = Depends(get_db),
    user_in: UserCreate,
) -> Any:
    try:
        print(f"\n=== REGISTRATION START ===")
        print(f"Received data: email={user_in.email}, name={user_in.name}")
        
        # Check if user exists
        print("Checking if user exists...")
        user = db.query(User).filter(User.email == user_in.email).first()
        if user:
            print(f"User already exists: {user_in.email}")
            raise HTTPException(
                status_code=400,
                detail="The user with this email already exists in the system",
            )
        print("User does not exist, proceeding...")
        
        # Hash password
        print(f"Hashing password of length: {len(user_in.password)}")
        hashed_password = security.get_password_hash(user_in.password)
        print(f"Password hashed successfully")
        
        # Create user
        print("Creating user object...")
        user = User(
            email=user_in.email,
            hashed_password=hashed_password,
            name=user_in.name,
            timezone=user_in.timezone if user_in.timezone else "UTC",
        )
        print(f"User object created: {user.email}")
        
        print("Adding user to database...")
        db.add(user)
        print("Committing...")
        db.commit()
        print("Refreshing...")
        db.refresh(user)
        print(f"User created successfully: {user.email}, ID: {user.id}")
        print(f"=== REGISTRATION SUCCESS ===\n")
        
        # Explicitly validate with Pydantic model to avoid validation errors
        return UserSchema.model_validate(user)
    except HTTPException:
        print("HTTPException raised, re-raising...")
        raise
    except Exception as e:
        print(f"\n=== REGISTRATION ERROR ===")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        import traceback
        traceback.print_exc()
        with open("registration_error.log", "w") as f:
            f.write(f"Error: {str(e)}\n")
            f.write(f"Error type: {type(e).__name__}\n")
            traceback.print_exc(file=f)
        print(f"=== REGISTRATION ERROR END ===\n")
        raise HTTPException(status_code=500, detail=f"Registration failed: {str(e)}")
