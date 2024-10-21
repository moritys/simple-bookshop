from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import CRUDBase
from models.book import Book


class CRUDBook(CRUDBase):

    async def get_book_id_by_name(
        self,
        book_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        db_book_id = await session.execute(
            select(Book.id).where(
                Book.name == book_name
            )
        )
        db_book_id = db_book_id.scalars().first()
        return db_book_id


book_crud = CRUDBook(Book)
