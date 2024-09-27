import os
from dataclasses import dataclass


@dataclass
class Config:
    app_title: str = 'Книжный магазин' # эти параметры тоже можно засунуть в переменные окружения
    app_description: str = 'Описание магазина'
    reload: bool = True

    host: str = os.getenv("APP_HOST", "127.0.0.1")
    port: int = int(os.getenv("APP_PORT", 8000))


def get_config() -> Config:
    return Config()
