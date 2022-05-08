from fastapi import APIRouter, Request
from typing import Optional
from app.models import CreateBookRequest

books_router = APIRouter(
    prefix="/api/books",
    tags=["books"],
    responses={404: {"message": "Reply not found"}}
)

@books.post("/")
async def create_books(payload: CreateBookRequest) -> str:
    pass
