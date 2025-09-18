from fastapi import APIRouter, Request
from utils.openrouter_client import get_ai_response

router = APIRouter()

@router.post("/therapy")
async def therapy(request: Request):
    data = await request.json()          # parse JSON body
    user_input = data.get("message")     # get 'message' key
    if not user_input:
        return {"response": "Please provide a message."}
    ai_response = get_ai_response(user_input)
    return {"response": ai_response}
