from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum as AEnum
from sqlalchemy.orm import relationship
from enum import Enum
from app.database import Base


class BookStatus(str, Enum):
    PRESENT = 'PRESENT'
    HOLD = 'HOLD'
    SOLD = 'SOLD'


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    status = Column(AEnum(BookStatus))

    bookshelve_id = Column(Integer, ForeignKey("bookshelves.id"))
    bookshelve = relationship("Bookshelve", back_populates="books")


class Bookshelve(Base):
    __tablename__ = "bookshelves"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, default=0, index=True)
    test = Column(String, default='')

    books = relationship("Book", back_populates="bookshelve")
