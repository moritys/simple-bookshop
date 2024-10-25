from fastapi import FastAPI

from api.endpoints.book import router as book_router
from api.endpoints.base import router as base_router
from api.endpoints.reservation import router as reservation_router
from api.endpoints.user import router as user_router


def setup_routers(app: FastAPI) -> None:
    app.include_router(book_router)
    app.include_router(base_router)
    app.include_router(reservation_router)
    app.include_router(user_router)
