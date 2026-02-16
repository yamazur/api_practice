from typing import List

from faker import Faker
from pydantic import BaseModel

fake = Faker()

class AdditionModel(BaseModel):
    additional_info: str
    additional_number: int

    @classmethod
    def fake(cls):
        """Создает фейковые данные для AdditionModel"""
        return cls(
            additional_info=fake.text(),
            additional_number=fake.random_int()
        )

class EntityModel(BaseModel):
    id: int | str | None = None
    addition: AdditionModel
    important_numbers: List[int]
    title: str
    verified: bool

    @classmethod
    def fake(cls, **kwargs):
        """
        Создает фейковую сущность

        Args:
            **kwargs: Поля для переопределения
        """
        return cls(
            addition=AdditionModel.fake(),
            important_numbers=list(fake.random_elements(
                elements=range(1, 100),
                length=3,
                unique=True
            )),
            title=fake.sentence(),
            verified=True,
            **kwargs  # переопределяем переданными значениями
        )

class EntityQueryModel(BaseModel):
    title: str | None = None
    verified: bool | None = None
    page: int | None = None
    perPage: int | None = None

    @classmethod
    def fake(cls):
        """Создает фейковые query параметры"""
        return cls(
            title=fake.word() if fake.boolean() else None,
            verified=fake.boolean() if fake.boolean() else None,
            page=fake.random_int(min=1, max=10) if fake.boolean() else None,
            perPage=fake.random_int(min=5, max=50) if fake.boolean() else None
        )
