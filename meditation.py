from fastapi import APIRouter
from models.user_data import meditation_collection

router = APIRouter()

@router.post("/meditation")
def add_meditation(data: dict):
    """
    Save a meditation session.
    Expected data: { "date": "YYYY-MM-DD", "minutes": 20 }
    """
    meditation_collection.insert_one(data)
    return {"status": "success"}

@router.get("/meditation")
def get_meditations():
    """
    Fetch all meditation sessions
    """
    return list(meditation_collection.find({}, {"_id": 0}))
