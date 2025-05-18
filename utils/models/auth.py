from typing_extensions import Self
from pydantic import BaseModel, Field, model_validator

from settings import settings


class AuthUser(BaseModel):
    username: str | None = Field(default=settings.test_user.email)
    password: str | None = Field(default=settings.test_user.password)


class Authentication(BaseModel):
    user: AuthUser | None = AuthUser()

    @model_validator(mode='after')
    def validate(self) -> Self:
        if not self.user:
            raise ValueError('Can not authenticate user, please provide "username"/"password"')

        return self
