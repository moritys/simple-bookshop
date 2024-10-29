from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_async_session
from app.crud.book import book_crud
from app.crud.reservation import reservation_crud
from app.schemas.book import BookCreate, BookDB, BookUpdate
from app.schemas.reservation import ReservationDB
from app.api.validators import check_book_exists, check_name_duplicate

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
    new_book = await book_crud.create(book, session)
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
    book = await check_book_exists(book_id, session)

    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)

    book = await book_crud.update(book, obj_in, session)
    return book


@router.get(
    '/',
    response_model=list[BookDB],
    response_model_exclude_none=True,
)
async def get_all_books(
    session: AsyncSession = Depends(get_async_session),
):
    book_list = await book_crud.get_multi(session)
    return book_list


@router.delete(
    '/{book_id}',
    response_model=BookDB,
    response_model_exclude_none=True,
)
async def remove_book(
    book_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    book = await check_book_exists(book_id, session)
    book = await book_crud.remove(book, session)
    return book


@router.get(
    '/{book_id}/reservations',
    response_model=list[ReservationDB],
)
async def get_reservations_for_book(
    book_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    await check_book_exists(book_id, session)
    reservations = await reservation_crud.get_future_reservations_for_book(
        book_id=book_id, session=session
    )
    return reservations
