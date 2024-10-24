from fastapi import FastAPI

import uvicorn
import uvicorn.server

from api import setup_routers
from core.config import get_config, Config


config: Config = get_config()


def build_app() -> FastAPI:
    app = FastAPI(
        title=config.app_title,
        description=config.app_description
    )
    setup_routers(app)
    print("💖")

    return app


def run_server():
    uvicorn.run(
        "main:build_app",
        factory=True,
        host=config.host,
        port=config.port,
        reload=config.reload
    )


if __name__ == '__main__':
    run_server()
