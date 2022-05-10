from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Enum as AEnum,
    text,
    update,
)
from sqlalchemy.event import listens_for
from sqlalchemy.types import DECIMAL
from sqlalchemy.orm import relationship
from enum import Enum
from app.database import Base
from app.database import get_db


class BookStatus(str, Enum):
    PRESENT = "PRESENT"
    HOLD = "HOLD"
    SOLD = "SOLD"


class Book(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False, index=True)
    price = Column(DECIMAL(7, 3))
    status = Column(AEnum(BookStatus))
    bookshelve_id = Column(Integer, ForeignKey("bookshelves.id"))
    bookshelve = relationship("Bookshelve", back_populates="books")


class Bookshelve(Base):

    __tablename__ = "bookshelves"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, default=0, index=True)
    books = relationship("Book", back_populates="bookshelve")


def get_status(price, bookshelve_id) -> BookStatus:

    if price and price > 0:
        return (
            BookStatus.PRESENT
            if bookshelve_id and bookshelve_id > 0
            else BookStatus.SOLD
        )

    return BookStatus.HOLD


@listens_for(Book, "before_insert")
def before_insert_function(mapper, connection, target):
    target.status = get_status(target.price, target.bookshelve_id)


@listens_for(Book, "after_update")
def after_update_book(mapper, connection, target):
    new_status = get_status(target.price, target.bookshelve_id)
    connection.execute(update(Book).where(Book.id == target.id), {"status": new_status})


@listens_for(Bookshelve, "after_delete")
def after_delete_bookshelve_update_book_status(mapper, connection, target):
    connection.execute(
        update(Book).where(Book.bookshelve_id == target.id, Book.price > 0),
        {"status": BookStatus.SOLD, "bookshelve_id": None},
    )
