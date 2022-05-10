from fastapi import Depends, APIRouter, Request, status
from typing import Optional
from app.models import (
    CreateBookRequest,
    UpdateBookRequest,
    CreateBookshelveRequest,
    Bookshelve,
    Book,
    BookStatus,
)
from app.database import get_db, update, create, delete, get
from sqlalchemy.orm import Session

books_router = APIRouter(
    prefix="/api/books", tags=["books"], responses={404: {"message": "Reply not found"}}
)


@books_router.post("/")
async def create_book(
    request: CreateBookRequest, db: Session = Depends(get_db)
) -> Book:

    return create(db, Book, request.dict())


@books_router.patch("/{book_id}")
async def update_book(
    book_id: int, request: UpdateBookRequest, db: Session = Depends(get_db)
) -> Book:

    return update(db, Book, book_id, request.dict(exclude_none=True))


@books_router.post("/bookshelve")
async def create_bookshelve(
    request: CreateBookshelveRequest, db: Session = Depends(get_db)
) -> Bookshelve:

    return create(db, Bookshelve, request.dict())


@books_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: int, db: Session = Depends(get_db)):

    return delete(db, Book, id)


@books_router.delete("/bookshelve/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: int, db: Session = Depends(get_db)):

    return delete(db, Bookshelve, id)


@books_router.get("/{book_id}")
async def create_book(book_id: int, db: Session = Depends(get_db)) -> Book:

    return get(db, Book, book_id)
