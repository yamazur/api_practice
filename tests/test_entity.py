import allure
import pytest

from conftest import api_entities
from entity.payloads import Payload


class TestEntities:

    @allure.title("Create new entity")
    def test_create_entity(self,created_entity):
        assert created_entity.id is not None

    @allure.title("Get entity")
    def test_get_entity(self, api_entities, created_entity):
        entity = api_entities.get_entity_by_id(created_entity.id)
        assert entity.id == created_entity.id

    @allure.title("Get all entities")
    def test_get_all_entities(self, api_entities, created_entity):
        entities = api_entities.get_all_entities()
        assert entities.total >= 0

    @allure.title("Update entity")
    def test_update_entity(self, api_entities, created_entity):
        update_payload = Payload.update_entity()
        updated_entity = api_entities.patch_entity_by_id(
            created_entity.id,
            payload=update_payload
        )
        assert updated_entity.title == update_payload["title"]

    @allure.title("Delete entity")
    def test_delete_entity(self, api_entities, created_entity):
        delete_entity = api_entities.delete_entity_by_id(created_entity.id)
        assert delete_entity == 204

        with pytest.raises(Exception):  # проверяем, что сущность действительно удалена
            api_entities.get_entity_by_id(created_entity.id)
