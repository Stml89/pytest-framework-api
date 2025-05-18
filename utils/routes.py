from enum import Enum


class APIRoutes(str, Enum):
    AUTH = '/auth'
    BOOKINGS = '/booking'

    def __str__(self) -> str:
        return self.value
