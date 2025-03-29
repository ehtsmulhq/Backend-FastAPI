from fastapi.exceptions import HTTPException
from fastapi import FastAPI,status
from pydantic import BaseModel
from typing import List


app= FastAPI()
 
books = [
    { "id": 1, "title": "1984", "author": "George Orwell", "published_year": 1949, "genre": "Dystopian"},
    { "id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "published_year": 1960, "genre": "Fiction"},
    { "id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "published_year": 1925, "genre": "Fiction"}    
    ]


class Book(BaseModel):
  id:int
  title:str
  author:str
  published_year:int
  genre:str

@app.get('/books',response_model=List[Book])
async def read_root():
  return books


class BookCreateModel(BaseModel):
    title:str
    author:str
    published_year:int
    genre:str

class BookUpdateModel(BaseModel):
    title:str
    author:str
    published_year:int
    genre:str
    
@app.post('/books',status_code=201)
async def create_book(book_data:BookCreateModel)->dict:
  new_book = book_data.model_dump()
  new_book["id"] = len(books) + 1
  books.append(new_book)
  return new_book

@app.get('/books/{book_id}',response_model=List[Book])
async def read_book(book_id:int):
  for book in books:
    if book["id"] == book_id:
      return [book]
  raise HTTPException(status_code =status.HTTP_404_NOT_FOUND,detail="Book not found")


@app.patch('/books/{book_id}',response_model=List[Book])
async def update_book(book_id: int, book_update: BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
          book["title"] = book_update.title
          book["author"] = book_update.author
          book["published_year"] = book_update.published_year
          book["genre"] = book_update.genre
          return [book]

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.delete('/books/{book_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
  for book in books:
    if book['id'] == book_id:
      books.remove(book)
      return
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")