# route_homepage.py

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os


templates = Jinja2Templates(directory="backend/templates")

general_pages_router = APIRouter()


@general_pages_router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("general_pages/homepage.html", {"request": request})
