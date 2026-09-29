from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from ..database import get_db
from ..models import User
from ..schemas import RegisterRequest, LoginRequest
from ..auth import hash_password, verify_password, create_token

router = APIRouter()

@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    email = str(data.email).lower().strip()
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    try:
        user = User(name=data.name.strip(), email=email, password_hash=hash_password(data.password))
        db.add(user)
        db.commit()
        db.refresh(user)
        return {"message": "Registration successful", "user_id": user.id}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered")
    except Exception as exc:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Registration failed: {exc}")

@router.post("/token")
def token(data: LoginRequest, db: Session = Depends(get_db)):
    email = str(data.email).lower().strip()
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"access_token": create_token(user.id), "token_type": "bearer"}

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return token(data, db)

@router.get("/session-info")
def session_info(user=Depends(__import__("app.auth", fromlist=["get_current_user"]).get_current_user)):
    return {"logged_in": True, "user_id": user.id, "name": user.name, "email": user.email}
