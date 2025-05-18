from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import TypeVar, Optional

T = TypeVar('T')


class TestUserCreds(BaseSettings):
    email: str = "example"
    password: str = "example"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
        env_nested_delimiter="__"
    )

    base_url: Optional[T] = "example"
    environment: str = "example"
    test_user: TestUserCreds = TestUserCreds()

    @property
    def api_url(self) -> str:
        return f'{self.base_url}'


settings = Settings()
