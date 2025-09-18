from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

# Initialize router
router = APIRouter()

# Templates directory
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@router.get("/get-started", response_class=HTMLResponse)
async def get_started(request: Request):
    """
    Render the Get Started page with navigation links
    """
    nav_links = {
        "AI Therapy": "/therapy",
        "Meditation": "/meditation",
        "Sleep Tracker": "/sleep",
        "Mood Tracker": "/mood"
    }

    return templates.TemplateResponse("get_started.html", {
        "request": request,
        "nav_links": nav_links
    })
