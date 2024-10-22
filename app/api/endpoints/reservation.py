from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_session
from crud.reservation import reservation_crud
from schemas.reservation import (
    ReservationDB, ReservationCreate,
)
from api.validators import check_book_exists, check_reservation_intersections

router = APIRouter(prefix='/reservations', tags=['Reservations'])


@router.post(
    '/',
    response_model=ReservationDB,
)
async def create_reservation(
    reservation: ReservationCreate,
    session: AsyncSession = Depends(get_async_session),
):
    await check_book_exists(reservation.book_id, session)
    await check_reservation_intersections(
        **reservation.model_dump(), session=session
    )
    new_reservation = await reservation_crud.create(reservation, session)
    return new_reservation
