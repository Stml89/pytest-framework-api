from http import HTTPStatus
from httpx import Response
from loguru import logger

from utils.models.auth import AuthUser
from utils.clients.http.client import APIClient
from utils.routes import APIRoutes


class AuthenticationClient(APIClient):
    def get_auth_token_api(self, payload: AuthUser) -> Response:
        logger.debug(f"Sending auth request")
        return self.client.post(url=f'{self.client.base_url}{APIRoutes.AUTH}',
                                json=payload.model_dump())

    def get_auth_token(self, payload: AuthUser) -> str:
        response = self.get_auth_token_api(payload)
        json_response = response.json()
        logger.debug(f"Response: {json_response}, status code {response.status_code}")

        assert response.status_code == HTTPStatus.OK
        assert json_response.get('token')

        return json_response['token']
