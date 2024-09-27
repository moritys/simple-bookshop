from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Книжный магазин'
    app_description: str = 'Описание магазина'

    class Config:
        env_file = '.env'


settings = Settings()
