from fastapi import APIRouter,status
from fastapi.exceptions import HTTPException
from typing import List
from src.books.data import books
from src.books.schemas import Book, BookCreateModel, BookUpdateModel


book_router=APIRouter()


@book_router.get('/',response_model=List[Book])
async def read_root():
  return books



    
@book_router.post('/',status_code=201)
async def create_book(book_data:BookCreateModel)->dict:
  new_book = book_data.model_dump()
  new_book["id"] = len(books) + 1
  books.append(new_book)
  return new_book

@book_router.get('/{book_id}',response_model=List[Book])
async def read_book(book_id:int):
  for book in books:
    if book["id"] == book_id:
      return [book]
  raise HTTPException(status_code =status.HTTP_404_NOT_FOUND,detail="Book not found")


@book_router.patch('/{book_id}',response_model=List[Book])
async def update_book(book_id: int, book_update: BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
          book["title"] = book_update.title
          book["author"] = book_update.author
          book["published_year"] = book_update.published_year
          book["genre"] = book_update.genre
          return [book]

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.delete('/{book_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
  for book in books:
    if book['id'] == book_id:
      books.remove(book)
      return
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")