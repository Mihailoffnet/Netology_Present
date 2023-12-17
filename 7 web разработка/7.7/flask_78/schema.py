from abc import ABC
from typing import Optional

import pydantic


class AbstractUser(pydantic.BaseModel, ABC):
    name: str
    password: str

    @classmethod
    def secure_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError(f"Minimal length of password is 8")
        return v


class CreateUser(pydantic.BaseModel):
    name: str
    password: str


class UpdateUser(pydantic.BaseModel):
    name: Optional[str]
    password: Optional[str]
