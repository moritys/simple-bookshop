from datetime import date

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import CRUDBase
from models.reservation import Reservation


class CRUDReservation(CRUDBase):

    async def get_reservation_at_the_same_time(
        self,
        from_reserve: date,
        to_reserve: date,
        book_id: int,
        session: AsyncSession,
    ) -> list[Reservation]:
        reservations = await session.execute(
            select(Reservation).where(
                Reservation.book_id == book_id,
                and_(
                    from_reserve <= Reservation.to_reserve,
                    to_reserve >= Reservation.from_reserve
                )
            )
        )  # не работает проверка пересечений, подумать (?)
        reservations = reservations.scalars().all()
        return reservations


reservation_crud = CRUDReservation(Reservation)
