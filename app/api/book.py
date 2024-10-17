from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_session
from crud.book import (
    create_book, get_book_id_by_name, read_all_books_from_db,
    get_book_by_id, update_book,
)
from schemas.book import BookCreate, BookDB, BookUpdate

router = APIRouter(prefix='/books', tags=['Books'])


@router.post(
    '/',
    response_model=BookDB,
    response_model_exclude_none=True,
)
async def create_new_book(
    book: BookCreate,
    session: AsyncSession = Depends(get_async_session),
):
    await check_name_duplicate(book.name, session)
    new_book = await create_book(book, session)
    return new_book


@router.patch(
    '/{book_id}',
    response_model=BookDB,
    response_model_exclude_none=True,
)
async def partially_update_book(
    book_id: int,
    obj_in: BookUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    book = await get_book_by_id(book_id, session)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail='Книга не найдена!'
        )

    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)

    book = await update_book(book, obj_in, session)
    return book


@router.get(
    '/',
    response_model=list[BookDB],
    response_model_exclude_none=True,
)
async def get_all_books(
    session: AsyncSession = Depends(get_async_session),
):
    book_list = await read_all_books_from_db(session)
    return book_list


async def check_name_duplicate(
    book_name: str,
    session: AsyncSession,
) -> None:
    book_id = await get_book_id_by_name(book_name, session)
    if book_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Переговорка с таким именем уже существует!',
        )
