import allure
from httpx import Response

from utils.models.booking import Booking
from utils.clients.http.client import APIClient
from utils.routes import APIRoutes


class BookerClient(APIClient):
    @allure.step(f'Getting all bookings ids')
    def get_all_bookings_api(self) -> Response:
        return self.client.get(APIRoutes.BOOKINGS)

    @allure.step('Creating booking')
    def create_booking_api(self, payload: Booking) -> Response:
        return self.client.post(APIRoutes.BOOKINGS,
                                json=payload.model_dump(by_alias=True))

    @allure.step('Getting booking with id "{booking_id}"')
    def get_booking_api(self, booking_id: int) -> Response:
        return self.client.get(f'{APIRoutes.BOOKINGS}/{booking_id}')

    @allure.step('Updating booking with id "{booking_id}"')
    def update_booking_api(self, booking_id: int, payload: Booking) -> Response:
        return self.client.put(f'{APIRoutes.BOOKINGS}/{booking_id}',
                               json=payload.model_dump(by_alias=True),
                               headers=self.client.headers)

    @allure.step('Deleting booking with id "{booking_id}"')
    def delete_booking_api(self, booking_id: int) -> Response:
        return self.client.delete(f'{APIRoutes.BOOKINGS}/{booking_id}')
