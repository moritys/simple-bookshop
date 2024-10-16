from fastapi import APIRouter, HTTPException

from crud.book import create_book, get_book_id_by_name
from schemas.book import BookCreate, BookDB

router = APIRouter()


@router.post(
    '/books/',
    response_model=BookDB,
    response_model_exclude_none=True,
)
async def create_new_book(
    book: BookCreate,
):
    book_id = await get_book_id_by_name(book.name)
    if book_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Книга с таким именем уже существует.'
        )
    new_book = await create_book(book)
    return new_book
