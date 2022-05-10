from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Enum as AEnum,
)
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

