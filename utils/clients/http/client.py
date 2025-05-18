import allure
from httpx import Client, Response
from httpx._types import URLTypes


class HTTPClient(Client):
    @allure.step('Making GET request to "{url}"')
    def get(self, url: URLTypes, *args: list, **kwargs: dict) -> Response:
        return super().get(url, *args, **kwargs)

    @allure.step('Making POST request to "{url}"')
    def post(self, url: URLTypes, *args: list, **kwargs: dict) -> Response:
        return super().post(url, *args, **kwargs)

    @allure.step('Making PUT request to "{url}"')
    def put(self, url: URLTypes, *args: list, **kwargs: dict) -> Response:
        return super().put(url, *args, **kwargs)

    @allure.step('Making DELETE request to "{url}"')
    def delete(self, url: URLTypes, *args: list, **kwargs: dict) -> Response:
        return super().delete(url, *args, **kwargs)


class APIClient:
    def __init__(self, client: HTTPClient) -> None:
        self._client = client

    @property
    def client(self) -> HTTPClient:
        return self._client
