import os
from dataclasses import dataclass


@dataclass
class Config:
    # эти параметры тоже можно засунуть в переменные окружения
    app_title: str = 'Аренда книг'
    app_description: str = (
        'Сервис, позволяющий взять любую книгу в аренду сроком от 1 месяца.'
    )
    reload: bool = True

    host: str = os.getenv('APP_HOST', '127.0.0.1')
    port: int = int(os.getenv('APP_PORT', 8000))

    db_url: str = os.getenv('DATABASE_URL', 'sqlite+aiosqlite:///./fastapi.db')


def get_config() -> Config:
    return Config()


# более красивый вариант определения url db

# # database_config.py

# @dataclass
# class DataBaseConfig:
#     host: str = os.getenv("DB_HOST")
#     port: int = int(os.getenv("DB_PORT"))
#     db_name: str = os.getenv("DB_NAME)
#     driver: str = os.getenv("DB_DRIVER")

#     @property
#     def url(self) -> str:
#         return f"{self.driver}://{self.host}:{self.port}/{self.db_name}"

# def get_db_config() -> DataBaseConfig:
#     return DataBaseConfig()

# # config.py

# from database_config import get_db_config
# @dataclass
# class Config:
#     ...
#     # и вытаскиваем URL уже из конфига нашей БД
#     db_url: str = get_db_config().url
