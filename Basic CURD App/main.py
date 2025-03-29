from fastapi import FastAPI
from pydantic import BaseModel


app= FastAPI()
 
books = [
    { "id": 1, "title": "1984", "author": "George Orwell", "published_year": 1949, "genre": "Dystopian"},
    { "id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "published_year": 1960, "genre": "Fiction"},
    { "id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "published_year": 1925, "genre": "Fiction"}    
    ]

@app.get('/books')
async def read_root():
  return books


class BookCreateModel(BaseModel):
    title:str
    author:str
    published_year:int
    genre:str
    
@app.post('/books')
async def create_book(book:BookCreateModel):
  new_book = book.dict()
  new_book["id"] = len(books) + 1
  books.append(new_book)
  return new_book

@app.get('/books/{book_id}')
async def read_book(book_id:int):
  for book in books:
    if book["id"] == book_id:
      return book
  return {"error": "Book not found"}

@app.put('/books/{book_id}')
async def update_book(book_id:int, book:BookCreateModel):
  for b in books:
    if b["id"] == book_id:
      b.update(book.dict())
      return b
  return {"error": "Book not found"}

@app.delete('/books/{book_id}')
async def delete_book(book_id:int):
  for book in books:
    if book["id"] == book_id:
      books.remove(book)
      return {"message": "Book deleted successfully"}
  return {"error": "Book not found"}