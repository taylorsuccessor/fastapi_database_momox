from sqlalchemy import update
from sqlalchemy.event import listens_for
from .books import Book, Bookshelve, BookStatus


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
