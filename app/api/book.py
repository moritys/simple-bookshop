from fastapi import APIRouter

from crud.book import create_book
from schemas.book import BookCreate

router = APIRouter()


@router.post('/books/')
async def create_new_book(
    book: BookCreate,
):
    new_book = await create_book(book)
    return new_book
