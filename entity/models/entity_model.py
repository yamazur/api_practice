from typing import List
from pydantic import BaseModel

class AdditionModel(BaseModel):
    additional_info: str
    additional_number: int

class EntityModel(BaseModel):
    id: int | str | None = None
    addition: AdditionModel
    important_numbers: List[int]
    title: str
    verified: bool

class EntityQueryModel(BaseModel):
    title: str | None = None
    verified: bool | None = None
    page: int | None = None
    perPage: int | None = None

# class EntityListResponse(BaseModel):
#     content: List[EntityModel]
#     total: int