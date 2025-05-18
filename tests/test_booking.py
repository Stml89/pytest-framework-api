import allure
from http import HTTPStatus
import pytest

from utils.api.booking import BookerClient
from utils.models.booking import (BookingsIdsList,
                                  Booking)
from utils.assertions import compare_dicts
from utils.assertions import assert_status_code
from utils.random_generator import random_number
from utils.validate.schema import validate_schema


@pytest.mark.api
@pytest.mark.bookings
@allure.feature('Bookings API')
@allure.story('CRUD for booking API')
class TestBookingsAPI:
    @allure.title('Get bookings')
    @allure.description("This test attempts to fetch all bookings IDs")
    def test_get_bookings(self, booker_client: BookerClient):
        response = booker_client.get_all_bookings_api()
        json_response = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_schema(json_response, BookingsIdsList.model_json_schema())

    @allure.title('Create new booking')
    @allure.description("This test attempts to create a new booking")
    def test_create_booking(self, booker_client: BookerClient):
        payload = Booking()

        response = booker_client.create_booking_api(payload)
        json_response = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        compare_dicts(expected_booking=json_response['booking'], actual_booking=payload)
        validate_schema(json_response, Booking.model_json_schema())

    @allure.title('Get booking by id')
    @allure.description("This test attempts to fetch particular booking by it's ID")
    def test_get_booking(self, booker_client: BookerClient):
        response = booker_client.get_booking_api(random_number())
        json_response = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_schema(json_response, Booking.model_json_schema())

    @allure.title('Update booking')
    @allure.description("This test attempts to update existing booking by it's ID")
    def test_update_booking(self, booker_client: BookerClient):
        payload = Booking()

        response = booker_client.update_booking_api(random_number(),
                                                    payload)
        json_response = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        compare_dicts(expected_booking=json_response, actual_booking=payload)

        validate_schema(json_response, Booking.model_json_schema())

    @allure.title('Delete booking')
    @allure.description("This test attempts to delete existing booking by it's ID")
    def test_delete_booking(self, booker_client: BookerClient):
        random_id = random_number()
        delete_booking_response = booker_client.delete_booking_api(random_id)
        get_booking_response = booker_client.get_booking_api(random_id)

        assert_status_code(delete_booking_response.status_code, HTTPStatus.CREATED)
        assert_status_code(get_booking_response.status_code, HTTPStatus.NOT_FOUND)
