from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class RegisterRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(min_length=6, max_length=100)

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class HomeRequest(BaseModel):
    budget: float = Field(gt=0)
    room: str
    style: str = "Modern"
    items: str = ""

class PartyRequest(BaseModel):
    budget: float = Field(gt=0)
    guests: int = Field(gt=0)
    event_type: str
    venue: str = "Any"
    preferences: str = ""

class JewelryRequest(BaseModel):
    budget: float = Field(gt=0)
    occasion: str
    style: str = "Elegant"
    outfit_description: str = ""
