from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from crud.book import book_crud
from crud.reservation import reservation_crud
from models.book import Book


async def check_name_duplicate(
    book_name: str,
    session: AsyncSession,
) -> None:
    book_id = await book_crud.get_book_id_by_name(book_name, session)
    if book_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Переговорка с таким именем уже существует!',
        )


async def check_book_exists(
    book_id: int,
    session: AsyncSession,
) -> Book:
    book = await book_crud.get(book_id, session)
    if book is None:
        raise HTTPException(
            status_code=404,
            detail='Книга не найдена!'
        )
    return book


async def check_reservation_intersections(**kwargs) -> None:
    reservations = await reservation_crud.get_reservation_at_the_same_time(
        **kwargs
    )
    if reservations:
        raise HTTPException(
            status_code=422,
            detail=str(reservations)
        )


async def check_reservation_before_edit(
    reservation_id: int, session: AsyncSession
):
    reservation = await reservation_crud.get(reservation_id, session)
    if not reservation:
        raise HTTPException(
            status_code=404,
            detail='Бронь не найдена!'
        )
    return reservation
