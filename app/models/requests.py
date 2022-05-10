from pydantic import BaseModel, condecimal, Field, validator
from typing import Optional
from decimal import Decimal
from app.database import get_db
from .books import Book, Bookshelve

class BaseBookRequest(BaseModel):

    title: Optional[str]
    price: condecimal(lt=10000, ge=0, max_digits=7, decimal_places=3) = Field(default=0)
    bookshelve_id: Optional[int]

    @validator('bookshelve_id')
    def exist_bookshelve_id(cls: BaseModel, v: str) -> str:
        db = next(get_db())
        bookshelve = db.query(Bookshelve).filter(Bookshelve.id==v).first()
        if not bookshelve and v:
            raise ValueError('Bookshelve not exist')
        return v


class CreateBookRequest(BaseBookRequest):

    title: str = Field(..., min_length=3)

    @validator('title')
    def unique_title(cls: BaseModel, v: str) -> str:
        db = next(get_db())
        exist = db.query(Book).filter(Book.title==v).first()
        if exist:
            raise ValueError('Title is already exist')
        return v


class UpdateBookRequest(BaseBookRequest):

    title: Optional[str]


class CreateBookshelveRequest(BaseModel):

    number: int = Field(min=0)
