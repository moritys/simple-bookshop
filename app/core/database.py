from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import Config, get_config

config: Config = get_config()


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


DATABASE_URL = config.db_url

Base = declarative_base(cls=PreBase)

engine = create_async_engine(
    DATABASE_URL, connect_args={'check_same_thread': False}
)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
