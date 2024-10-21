from .base import CRUDBase
from models.reservation import Reservation


reservation_crud = CRUDBase(Reservation)
