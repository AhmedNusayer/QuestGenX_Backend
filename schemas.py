from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from pydantic.types import conint

T = TypeVar('T')

class QASchema(BaseModel):
    id: int
    userId: str
    examId: int
    question: str
    options: List[str]

    class Config:
        orm_mode = True

