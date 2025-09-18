from fastapi import APIRouter
from models.user_data import mood_collection

router = APIRouter()

@router.post("/mood")
def add_mood(data: dict):
    mood_collection.insert_one(data)
    return {"status": "success"}

@router.get("/mood")
def get_moods():
    return list(mood_collection.find({}, {"_id": 0}))
