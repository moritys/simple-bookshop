from sqlalchemy import Column, Date, ForeignKey, Integer

from .base import Base


class Reservation(Base):
    from_reserve = Column(Date)
    to_reserve = Column(Date)
    book_id = Column(Integer, ForeignKey('book.id'))
