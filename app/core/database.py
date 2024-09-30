from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

import os

from dotenv import load_dotenv

load_dotenv('.env')


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


# урл бд храним в енв или тут?
# DATABASE_URL = 'sqlite:///./sql_app.db'
DATABASE_URL = os.environ['DATABASE_URL']
# DATABASE_URL = 'postgresql://user:password@postgresserver/db'

Base = declarative_base(cls=PreBase)

engine = create_async_engine(
    DATABASE_URL, connect_args={'check_same_thread': False}
)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
