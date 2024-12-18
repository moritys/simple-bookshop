from datetime import date
from typing import Optional

from pydantic import BaseModel, model_validator, field_validator, ConfigDict


class ReservationBase(BaseModel):
    from_reserve: date
    to_reserve: date

    # запрет на передачу других полей
    model_config = ConfigDict(extra='forbid')


class ReservationUpdate(ReservationBase):

    @field_validator('from_reserve')
    def ckeck_from_reserve_later_than_now(cls, value):
        if value < date.today():
            raise ValueError(
                'Время начала бронирования '
                'не может быть меньше текущего времени'
            )
        return value

    @model_validator(mode='before')
    def check_from_reserve_before_to_reserve(cls, values):
        if values['from_reserve'] >= values['to_reserve']:
            raise ValueError(
                'Время начала бронирования '
                'не может быть больше времени окончания'
            )
        return values


class ReservationCreate(ReservationUpdate):
    book_id: int


class ReservationDB(ReservationBase):
    id: int
    book_id: int
    user_id: Optional[int]

    class Config:
        from_attributes = True
