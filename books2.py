from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(None, description="id is optional")
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

    class Config:
        schema_extra = {
            "example": "A new Book",
            "author": "CodingWithGarry",
            "description": "Some insane Book",
            "rating": 5,
        }


BOOKS = [
    Book(1, "Computer Science Book", "Dereck John", "A comprehensive book", 5),
    Book(2, "Chemistry Practice Guide", "Jonathan Dereck", "A great book", 4),
    Book(3, "Social Science Book", "Dheere Dereck John", "A nice book", 1),
    Book(4, "Lua Science Book", "Dereck John", "A lucid book", 3),
    Book(5, "Python Science Book", "Dereck John", "A awesome book", 2),
    Book(6, "Go Science Book", "Dereck John", "A star book", 5),
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    # msg = {"msg": "A New Book Created"}
    return book_request


@app.get("/books/{book_id}")
def find_book_id(book_id: int):
    for book in BOOKS:
        print(book.id)
        if book.id == book_id:
            return BOOKS[book.id]


@app.get("/books/")
async def read_book_by_rating(book_rating: int):
    for book in BOOKS:
        if book.rating == book_rating:
            return book
    else:
        return {"msg": f"Book of rating {book_rating} not found, Plz try again"}
