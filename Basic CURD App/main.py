import json
from fastapi import FastAPI
from pydantic import BaseModel


app= FastAPI()

with open("books.json", "r") as file:
    books = json.load(file)
    

@app.get('/')
async def read_root():
  return books


class BookCreateModel(BaseModel):
    title:str
    author:str
    published_year:int
    genre:str
    
@app.post('/create_book')
async def create_book(book:BookCreateModel):
  new_book = book.dict()
  new_book["id"] = len(books) + 1  
  books.append(new_book)
  return new_book