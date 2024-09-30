from fastapi import FastAPI

import uvicorn
import uvicorn.server

from api.endpoints import router
from core.config import get_config, Config


config: Config = get_config()


def build_app() -> FastAPI:
    app = FastAPI(
        title=config.app_title,
        description=config.app_description
    )
    app.include_router(router)
    print('💖')

    return app


if __name__ == '__main__':
    uvicorn.run(
        "main:build_app",
        factory=True,
        host=config.host,
        port=config.port,
        reload=config.reload
    )
