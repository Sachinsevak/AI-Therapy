from fastapi import APIRouter
from models.user_data import sleep_collection

router = APIRouter()

@router.post("/sleep")
def add_sleep(data: dict):
    """
    Save sleep data.
    Expected data: { "date": "YYYY-MM-DD", "hours": 7 }
    """
    sleep_collection.insert_one(data)
    return {"status": "success"}

@router.get("/sleep")
def get_sleep_logs():
    """
    Fetch all sleep logs
    """
    return list(sleep_collection.find({}, {"_id": 0}))
