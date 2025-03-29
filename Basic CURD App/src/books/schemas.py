from pydantic import BaseModel


class Book(BaseModel):
  id:int
  title:str
  author:str
  published_year:int
  genre:str

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
    
    
