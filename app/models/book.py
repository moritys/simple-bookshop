from sqlalchemy import Column, String

from .base import Base


class Book(Base):
    name = Column(String(100), nullable=False)
