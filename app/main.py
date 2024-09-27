from fastapi import FastAPI

import uvicorn

from api.endpoints import router
from core.config import settings

app = FastAPI(title=settings.app_title, description=settings.app_description)

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
