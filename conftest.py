import pytest
from entity.api_entity import EntityAPI
from entity.payloads import Payload


@pytest.fixture
def api_entities(api_users):
    return EntityAPI()

@pytest.fixture(scope="module")
def created_entity(api_users):
    payload = Payload.create_entity()
    entity = api_users.create_entity(payload)
    return entity