from loguru import logger
import pytest

from utils.api.booking import BookerClient
from utils.models.auth import Authentication
from utils.clients.http.builder import get_http_client


@pytest.fixture(scope="class")
def booker_client() -> BookerClient:
    logger.debug(f"Creating a client to communicate with booking API")
    return BookerClient(
        client=get_http_client(auth=Authentication())
    )
