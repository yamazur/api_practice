from typing import List
from pydantic import BaseModel

class AdditionModel(BaseModel):
    additional_info: str
    additional_number: int

class EntityModel(BaseModel):
    id: int | None = None
    addition: AdditionModel
    important_numbers: List[int]
    title: str
    verified: bool
