from sqlalchemy import Column, String, Text

from .base import Base


class Book(Base):
    name = Column(String(100), nullable=False)
    description = Column(Text)
