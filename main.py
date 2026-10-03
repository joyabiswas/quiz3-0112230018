from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    title: str
    author: str
    price: float


books = []


@app.get("/books")
def get_books():
    return books


@app.post("/books", status_code=201)
def create_book(book: Book):
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author,
        "price": book.price
    }

    books.append(new_book)
    return new_book


@app.put("/books/{id}")
def update_book(id: int, book: Book):
    for existing_book in books:
        if existing_book["id"] == id:
            existing_book["title"] = book.title
            existing_book["author"] = book.author
            existing_book["price"] = book.price
            return existing_book

    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{id}")
def delete_book(id: int):
    for existing_book in books:
        if existing_book["id"] == id:
            books.remove(existing_book)
            return existing_book

    raise HTTPException(status_code=404, detail="Book not found")