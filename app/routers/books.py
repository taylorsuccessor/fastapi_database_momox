from fastapi import Depends, APIRouter, Request, status
from typing import Optional
from app.models import CreateBookRequest, UpdateBookRequest, CreateBookshelveRequest, Bookshelve, Book, BookStatus, get_status
from app.database import get_db, update
from sqlalchemy.orm import Session

books_router = APIRouter(
    prefix="/api/books",
    tags=["books"],
    responses={404: {"message": "Reply not found"}}
)

@books_router.post("/")
async def create_book(request: CreateBookRequest, db: Session=Depends(get_db)) -> Book:

    book = Book(**request.dict())
    book.status = get_status(request.price, request.bookshelve_id)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

@books_router.patch("/{book_id}")
async def update_book(book_id: int, request: UpdateBookRequest, db: Session=Depends(get_db)) -> Book:

    book = update(db, Book, book_id, request.dict(exclude_none=True))
    return book


@books_router.post("/bookshelve")
async def create_bookshelve(request: CreateBookshelveRequest, db: Session=Depends(get_db)) -> Bookshelve:

    bookshelve = Bookshelve(**request.dict())
    db.add(bookshelve)
    db.commit()
    db.refresh(bookshelve)
    return bookshelve


@books_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: int, db: Session=Depends(get_db)):

    book = db.query(Book).get(id)

    if book:
        db.delete(book)
        db.commit()
        db.close()
    else:
        raise HTTPException(status_code=404, detail=f"Book with id {id} not found")

    return None


@books_router.delete("/bookshelve/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: int, db: Session=Depends(get_db)):

    bookshelve = db.query(Bookshelve).get(id)

    if bookshelve:
        db.delete(bookshelve)
        db.commit()
        db.close()
    else:
        raise HTTPException(status_code=404, detail=f"Bookshelve with id {id} not found")

    return None
