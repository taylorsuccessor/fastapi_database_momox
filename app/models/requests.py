from pydantic import BaseModel


class CreateBookRequest(BaseModel):

    title: str


class CreateBookshelveRequest(BaseModel):

    number: int
