from __future__ import annotations
import datetime

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    summary: str | None = None
    publication_date: datetime.date


class BookCreate(BookBase):
    author_id: int


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    name: str
    bio: str | None = None


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int
    books: list[Book] = []

    class Config:
        orm_mode = True
