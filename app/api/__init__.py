from fastapi import FastAPI

from .book import router as book_router
from .base import router as base_router


def setup_routers(app: FastAPI) -> None:
    app.include_router(book_router)
    app.include_router(base_router)
