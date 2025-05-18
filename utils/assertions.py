import allure
from http import HTTPStatus
from enum import Enum
from typing import TypeVar
from utils.models.booking import (Booking)

T = TypeVar('T')


class AssertionTypes(str, Enum):
    EQUAL = '=='


class AssertionBase:
    def __init__(self, expected: HTTPStatus) -> None:
        self.expected = expected
        self._description = None
        self._step = allure.step

    def set_error_description(self, description: str) -> None:
        self._description = description

    def _error_message(self, actual: T, method: AssertionTypes) -> str:
        return f"""Checking: {self._description}
               Expected: {self.expected} {type(self.expected)}
               Actual: {actual} {type(actual)}
               Expression: assert {self.expected} {method} {actual}"""


class Assertions(AssertionBase):
    def to_be_equal(self, actual: T) -> None:
        step_name = f'Checking that "{self._description}" equals to "{self.expected}"'
        with self._step(step_name):
            template = self._error_message(actual, AssertionTypes.EQUAL)
            assert self.expected == actual, template


def assert_status_code(actual: int, expected: HTTPStatus) -> None:
    assert_values(expected, actual, 'Status code')


def expect(expected: T) -> Assertions:
    return Assertions(expected=expected)


def assert_values(actual: int | str, expected: int | str, description: str) -> None:
    e = expect(expected)
    e.set_error_description(description)
    e.to_be_equal(actual)


def compare_dicts(expected_booking: Booking, actual_booking: Booking) -> None:
    assert_values(expected_booking['firstname'],
                  actual_booking.firstname,
                  'Field "First name"')
    assert_values(expected_booking['lastname'],
                  actual_booking.lastname,
                  'Field "Last name"')
    assert_values(expected_booking['totalprice'],
                  actual_booking.totalprice,
                  'Field "Total price"')
    assert_values(expected_booking['depositpaid'],
                  actual_booking.depositpaid,
                  'Field "Is deposit paid"')
