import json
from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import RecommendationHistory
from ..auth import get_current_user
from ..schemas import HomeRequest, PartyRequest, JewelryRequest
from ..recommendations import home_fallback, party_fallback, jewelry_fallback
from ..gemini_utils import generate_with_gemini, build_prompt

router = APIRouter()

def save_history(db, user_id, category, request_data, response):
    row = RecommendationHistory(
        user_id=user_id, category=category,
        request_data=json.dumps(request_data),
        response_data=json.dumps(response)
    )
    db.add(row); db.commit()

@router.post("/generate-home")
def generate_home(data: HomeRequest, db: Session = Depends(get_db), user=Depends(get_current_user)):
    payload = data.model_dump()
    ai = generate_with_gemini(build_prompt("Home Interior", payload))
    response = {"ai_response": ai} if ai else home_fallback(payload)
    save_history(db, user.id, "Home", payload, response)
    return response

@router.post("/generate-party")
def generate_party(data: PartyRequest, db: Session = Depends(get_db), user=Depends(get_current_user)):
    payload = data.model_dump()
    ai = generate_with_gemini(build_prompt("Party Planning", payload))
    response = {"ai_response": ai} if ai else party_fallback(payload)
    save_history(db, user.id, "Party", payload, response)
    return response

@router.post("/generate-jewelry")
async def generate_jewelry(
    budget: float = Form(...), occasion: str = Form(...),
    style: str = Form("Elegant"), outfit_description: str = Form(""),
    outfit_image: UploadFile | None = File(None),
    db: Session = Depends(get_db), user=Depends(get_current_user)
):
    payload = {"budget": budget, "occasion": occasion, "style": style, "outfit_description": outfit_description}
    image_bytes = await outfit_image.read() if outfit_image else None
    ai = generate_with_gemini(build_prompt("Jewelry", payload), image_bytes)
    response = {"ai_response": ai} if ai else jewelry_fallback(payload)
    save_history(db, user.id, "Jewelry", payload, response)
    return response

@router.get("/history")
def history(db: Session = Depends(get_db), user=Depends(get_current_user)):
    rows = db.query(RecommendationHistory).filter(
        RecommendationHistory.user_id == user.id
    ).order_by(RecommendationHistory.created_at.desc()).all()
    return [
        {"id": r.id, "category": r.category, "request": json.loads(r.request_data),
         "response": json.loads(r.response_data), "created_at": r.created_at.isoformat()}
        for r in rows
    ]
