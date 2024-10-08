from typing import Optional

from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    name: str = Field(..., max_length=100)
    description: Optional[str]
