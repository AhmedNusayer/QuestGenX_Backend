from typing import TypeVar
from pydantic import BaseModel, Field


T = TypeVar('T')

class UserSchema(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True


class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)

