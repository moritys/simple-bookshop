from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import Config, get_config

config: Config = get_config()


DATABASE_URL = config.db_url

engine = create_async_engine(
    DATABASE_URL, connect_args={'check_same_thread': False}
)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
