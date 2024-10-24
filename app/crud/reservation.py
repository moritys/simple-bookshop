from datetime import date
from typing import Optional

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import CRUDBase
from models.reservation import Reservation


class CRUDReservation(CRUDBase):

    async def get_reservation_at_the_same_time(
        self,
        *,
        from_reserve: date,
        to_reserve: date,
        book_id: int,
        reservation_id: Optional[int],
        session: AsyncSession,
    ) -> list[Reservation]:
        select_stmt = select(Reservation).where(
            Reservation.book_id == book_id,
            and_(
                from_reserve <= Reservation.to_reserve,
                to_reserve >= Reservation.from_reserve
            )
        )  # не работает проверка пересечений, подумать (?)
        if reservation_id is not None:
            select_stmt = select_stmt.where(
                Reservation.id != reservation_id
            )
        reservations = await session.execute(select_stmt)
        reservations = reservations.scalars().all()
        return reservations

    async def get_future_reservations_for_book(
        book_id: int,
        session: AsyncSession,
    ) -> list[Reservation]:
        select_stmt = select(Reservation).where(
            Reservation.book_id == book_id,
            Reservation.to_reserve >= date.today()
        )

        reservations = await session.execute(select_stmt)
        reservations = reservations.scalars().all()
        return reservations


reservation_crud = CRUDReservation(Reservation)
