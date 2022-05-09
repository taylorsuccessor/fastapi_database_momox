from fastapi import Depends, APIRouter, Request
from typing import Optional
from app.models import CreateBookRequest, CreateBookshelveRequest, Bookshelve
from app.database import get_db
from sqlalchemy.orm import Session

books_router = APIRouter(
    prefix="/api/books",
    tags=["books"],
    responses={404: {"message": "Reply not found"}}
)

@books_router.post("/")
async def create_books(payload: CreateBookRequest) -> str:
    pass

@books_router.post("/bookshelve")
async def create_bookshelve(request: CreateBookshelveRequest, db: Session=Depends(get_db)) -> str:

    bookshelve = Bookshelve(number=request.number)
    db.add(bookshelve)
    db.commit()
    db.refresh(bookshelve)
    return bookshelve
