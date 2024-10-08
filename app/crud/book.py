from core.database import AsyncSessionLocal
from models.book import Book
from schemas.book import BookCreate


async def create_book(
    new_book: BookCreate
) -> Book:
    new_book_data = new_book.dict()
    db_book = Book(**new_book_data)

    async with AsyncSessionLocal as session:
        session.add(db_book)

        await session.commit()

        await session.refresh(db_book)

    return db_book
