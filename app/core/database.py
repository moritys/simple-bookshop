from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from .config import Config, get_config

config: Config = get_config()


DATABASE_URL = config.db_url

engine = create_async_engine(
    DATABASE_URL, connect_args={'check_same_thread': False}
)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
