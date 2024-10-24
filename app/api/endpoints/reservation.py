from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_session
from crud.reservation import reservation_crud
from schemas.reservation import (
    ReservationDB, ReservationCreate, ReservationUpdate
)
from api.validators import (
    check_book_exists, check_reservation_intersections,
    check_reservation_before_edit
)

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


@router.get(
    '/',
    response_model=list[ReservationDB],
)
async def get_all_reservations(
    session: AsyncSession = Depends(get_async_session),
):
    reservations = await reservation_crud.get_multi(session)
    return reservations


@router.delete(
    '/{reservation_id}',
    response_model=ReservationDB,
    response_model_exclude_none=True,
)
async def delete_reservation(
    reservation_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    reservation = await check_reservation_before_edit(reservation_id, session)
    reservation = await reservation_crud.remove(reservation, session)
    return reservation


@router.patch(
    '/{reservation_id}',
    response_model=ReservationDB
)
async def update_reservation(
    reservation_id: int,
    obj_in: ReservationUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    reservation = await reservation_crud.get(reservation_id, session)
    await check_reservation_intersections(
        **obj_in.model_dump(),
        reservation_id=reservation_id,
        book_id=reservation.book_id,
        session=session
    )
    reservation = await reservation_crud.update(
        db_obj=reservation,
        obj_in=obj_in,
        session=session
    )
    return reservation
