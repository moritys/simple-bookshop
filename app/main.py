from fastapi import FastAPI

import uvicorn
import uvicorn.server

from app.api import setup_routers
from app.core.config import get_config, Config
# from app.core.init_db import create_first_superuser


config: Config = get_config()


def build_app() -> FastAPI:
    app = FastAPI(
        title=config.app_title,
        description=config.app_description
    )
    setup_routers(app)
    print("💖")

    return app


# создание суперюзера при старте приложения
# подумать как прикрутить
# @app.on_event('startup')
# async def startup():
#     await create_first_superuser()


def run_server():
    uvicorn.run(
        "app.main:build_app",
        factory=True,
        host=config.host,
        port=config.port,
        reload=config.reload
    )
