import pytest
from entity.api_entity import EntityAPI
from entity.payloads import Payload


@pytest.fixture
def api_entities():
    return EntityAPI()

@pytest.fixture
def create_entity(api_entities):
    payload = Payload.create_entity()
    entity_id = api_entities.create_entity(payload)
    entity = api_entities.get_entity_by_id(entity_id)
    return entity