import pytest
from entity.api_entity import EntityAPI
from entity.models.entity_model import EntityModel
from entity.payloads import Payload


@pytest.fixture
def api_entities():
    return EntityAPI()

@pytest.fixture
def create_entity(api_entities):
    """Фикстура для создания тестовой сущности"""
    payload = EntityModel.fake()  # ✅ используем Pydantic модель
    entity = api_entities.create_entity(payload)
    yield entity