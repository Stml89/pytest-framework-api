from settings import settings
from utils.api.auth import AuthenticationClient
from utils.models.auth import Authentication
from utils.clients.http.client import HTTPClient


def get_http_client(auth: Authentication = None,
                    base_url: str = settings.api_url) -> HTTPClient:
    headers = {'Content-Type': 'application/json'}

    auth_client = AuthenticationClient(
        client=HTTPClient(base_url=base_url))

    token = auth_client.get_auth_token(auth.user)
    headers = {**headers, 'Cookie': f'token={token}'}

    return HTTPClient(base_url=base_url, headers=headers, trust_env=True)
