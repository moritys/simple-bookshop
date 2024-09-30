from sqlalchemy import Column, String

from core.database import Base


class Book(Base):
    name = Column(String(100), nullable=False)
