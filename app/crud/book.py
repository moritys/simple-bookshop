from typing import Optional

from fastapi.encoders import jsonable_encoder

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.book import Book
from schemas.book import BookCreate, BookUpdate


async def create_book(
    new_book: BookCreate,
    session: AsyncSession,
) -> Book:
    new_book_data = new_book.model_dump()
    db_book = Book(**new_book_data)

    session.add(db_book)
    await session.commit()
    await session.refresh(db_book)
    return db_book


async def get_book_id_by_name(
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


async def read_all_books_from_db(
    session: AsyncSession,
) -> list[Book]:
    book_list = await session.execute(select(Book))
    book_list = book_list.scalars().all()
    return book_list


async def get_book_by_id(
    book_id: int,
    session: AsyncSession,
) -> Optional[Book]:
    db_book = await session.execute(
        select(Book).where(
            Book.id == book_id
        )
    )
    db_book = db_book.scalars().first()
    return db_book


async def update_book(
    db_book: Book,
    book_in: BookUpdate,
    session: AsyncSession,
) -> Book:
    obj_data = jsonable_encoder(db_book)
    update_data = book_in.model_dump(exclude_unset=True)

    for field in obj_data:
        if field in update_data:
            setattr(db_book, field, update_data[field])

    session.add(db_book)
    await session.commit()
    await session.refresh(db_book)
    return db_book


async def delete_book(
    db_book: Book,
    session: AsyncSession,
) -> Book:
    await session.delete(db_book)
    await session.commit()
    return db_book
