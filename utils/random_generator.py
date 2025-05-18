from datetime import date, timedelta
from random import choice, randint
from string import ascii_letters, digits


def random_number(start: int = 1, end: int = 10) -> int:
    return randint(start, end)


def random_string(start: int = 9, end: int = 15) -> str:
    return ''.join(choice(ascii_letters + digits) for _ in range(randint(start, end)))


def random_list_of_strings(start: int = 9, end: int = 15) -> list[str]:
    return [random_string() for _ in range(randint(start, end))]


def random_boolean() -> bool:
    return choice([True, False])


def random_checkin_date() -> str:
    return date.today().strftime('%Y-%m-%d')


def random_checkout_date(d: int = 10) -> str:
    from_date = date.today() + timedelta(days=d)
    return from_date.strftime('%Y-%m-%d')
