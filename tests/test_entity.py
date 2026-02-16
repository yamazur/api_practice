import allure

from conftest import api_entities
from entity.models.entity_model import EntityModel


class TestEntity:

    @allure.title("Create new entity")
    def test_create_entity(self, api_entities, create_entity):
        assert create_entity.id is not None
        api_entities.delete_entity_by_id(create_entity.id)

    @allure.title("Get entity")
    def test_get_entity(self, api_entities, create_entity):
        entity = api_entities.get_entity_by_id(create_entity.id)
        assert entity.id == create_entity.id
        api_entities.delete_entity_by_id(create_entity.id)

    @allure.title("Get all entities")
    def test_get_all_entities(self, api_entities, create_entity):
        entities = api_entities.get_all_entity()
        assert entities is not None
        api_entities.delete_entity_by_id(create_entity.id)

    @allure.title("Update entity")
    def test_update_entity(self, api_entities, create_entity):
        update_payload = EntityModel.fake()

        # Метод вернёт обновлённую сущность после GET
        updated_entity = api_entities.patch_entity_by_id(
            create_entity.id,
            payload=update_payload
        )
        # Проверяем, что поле обновилось
        assert updated_entity.title == update_payload["title"]
        api_entities.delete_entity_by_id(create_entity.id)

    @allure.title("Delete entity")
    def test_delete_entity(self, api_entities, create_entity):
        delete_entity = api_entities.delete_entity_by_id(create_entity.id)
        assert delete_entity == 204
