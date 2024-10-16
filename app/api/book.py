from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_session
from crud.book import create_book, get_book_id_by_name, read_all_books_from_db
from schemas.book import BookCreate, BookDB

router = APIRouter()


@router.post(
    '/books/',
    response_model=BookDB,
    response_model_exclude_none=True,
)
async def create_new_book(
    book: BookCreate,
    session: AsyncSession = Depends(get_async_session),
):
    book_id = await get_book_id_by_name(book.name, session)
    if book_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Книга с таким именем уже существует.'
        )
    new_book = await create_book(book, session)
    return new_book


@router.get(
    '/books/',
    response_model=list[BookDB],
    response_model_exclude_none=True,
)
async def get_all_books(
    session: AsyncSession = Depends(get_async_session),
):
    book_list = await read_all_books_from_db(session)
    return book_list
