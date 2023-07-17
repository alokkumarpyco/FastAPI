from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "science"},
    {"title": "Title Five", "author": "Author Five", "category": "science"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
]


@app.get("/api-endpoint")
async def first_app():
    return BOOKS


@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
    else:
        return "Book Not Found"


@app.get("/books/")
async def read_category_by_query(category: str):
    book_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            book_to_return.append(book)
    return book_to_return
