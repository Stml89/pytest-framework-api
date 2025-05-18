from pydantic import BaseModel, Field, RootModel

from utils.random_generator import (random_number,
                                    random_string,
                                    random_boolean,
                                    random_checkin_date,
                                    random_checkout_date)


class Dates(BaseModel):
    checkin: str | None = Field(default_factory=random_checkin_date)
    checkout: str | None = Field(default_factory=random_checkout_date)


class Booking(BaseModel):
    firstname: str | None = Field(default_factory=random_string)
    lastname: str | None = Field(default_factory=random_string)
    totalprice: int | None = Field(default_factory=random_number)
    depositpaid: bool | None = Field(default_factory=random_boolean)
    bookingdates: Dates = Dates()
    additionalneeds: str | None = Field(default_factory=random_string)


class BookingIds(BaseModel):
    bookingid: int | None = Field(default_factory=random_number)


class BookingsIdsList(RootModel):
    root: list[BookingIds]
