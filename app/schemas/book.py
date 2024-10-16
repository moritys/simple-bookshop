from typing import Optional

from pydantic import BaseModel, Field


class BookBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]


class BookCreate(BookBase):
    name: str = Field(..., min_length=1, max_length=100)


class BookDB(BookBase):
    id: int

    class Config:
        from_attributes = True
