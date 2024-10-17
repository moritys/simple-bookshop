from typing import Optional

from pydantic import BaseModel, Field, field_validator


class BookBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]


class BookCreate(BookBase):
    name: str = Field(..., min_length=1, max_length=100)


class BookUpdate(BookBase):

    @field_validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Имя книги не может быть пустым!')
        return value


class BookDB(BookBase):
    id: int

    class Config:
        from_attributes = True
