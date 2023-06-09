from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from pydantic.types import conint

T = TypeVar('T')

class UserSchema(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True


class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)

