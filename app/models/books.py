from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    status = Column(String)

    bookshelve_id = Column(Integer, ForeignKey("bookshelves.id"))
    bookshelve = relationship("Bookshelve", back_populates="books")

class Bookshelve(Base):
    __tablename__ = "bookshelves"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, default=0, index=True)
    test = Column(String, default='')

    books = relationship("Book", back_populates="bookshelve")
