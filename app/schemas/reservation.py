from datetime import date

from pydantic import BaseModel, model_validator, field_validator


class ReservationBase(BaseModel):
    from_reserve: date
    to_reserve: date


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

    class Config:
        from_attributes = True
