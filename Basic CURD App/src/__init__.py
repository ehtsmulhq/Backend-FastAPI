from fastapi import FastAPI
from src.books.routers import book_router

version="v1"

app =FastAPI(
    
    version=version
)



app.include_router(book_router, prefix="/api/{version}/books")
