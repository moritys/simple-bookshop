from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declared_attr


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
# SQLALCHEMY_DATABASE_URL = 'postgresql://user:password@postgresserver/db'

Base = declarative_base(cls=PreBase)

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
