from fastapi import APIRouter, Body


router = APIRouter()


@router.get("/")
async def healthcheck() -> dict[str, str]:
    return {"status": "💖"}
