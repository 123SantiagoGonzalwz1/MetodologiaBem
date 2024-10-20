from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Book(BaseModel):
    title: str
    autor: str
    pages: int
    editorial: Optional[str]

@app.get("/")
def index():
    return {"message": "Hola, Pythonianos"}

@app.get("/books/{id}")
def getBooks(id: int):
    return { "data" : id }

@app.post("/books")
def createBooks(book: Book):
    return { "message": f"Libro: {book} creado" }