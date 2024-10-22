from sqlalchemy import Column, Date, ForeignKey, Integer

from .base import Base


class Reservation(Base):
    from_reserve = Column(Date)
    to_reserve = Column(Date)
    book_id = Column(Integer, ForeignKey('book.id'))

    def __repr__(self):
        return (
            f'Уже забронировано с {self.from_reserve} по {self.to_reserve}'
        )
