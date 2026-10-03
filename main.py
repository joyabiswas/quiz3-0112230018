from fastapi import FastAPI
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
    books.append(book)
    return book