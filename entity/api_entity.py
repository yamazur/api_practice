import allure
import requests

from config.headers import Headers
from utils.helper import Helper
from entity.payloads import Payload
from entity.endpoints import Endpoint
from entity.models.entity_model import EntityModel, EntityQueryModel, EntityListResponse


class EntityAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = Payload()
        self.endpoints = Endpoint()
        self.headers = Headers()

    @allure.step("Создание сущности")
    def create_entity(self, payload):
        response = requests.post(
            url=self.endpoints.CREATE,
            headers=self.headers.basic,
            json=payload,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = EntityModel(**response.json())
        return model

    @allure.step("Получение сущности по ID")
    def get_entity_by_id(self, entity_id):
        response = requests.get(
            url=self.endpoints.GET_BY_ID(entity_id),
            headers=self.headers.basic,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = EntityModel(**response.json())
        return model

    @allure.step("Получение списка сущностей")
    def get_all_entity(self, query=None):
        response = requests.get(
            url=self.endpoints.GET_ALL,
            params=query.model_dump(exclude_none=True) if query else None
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = EntityListResponse(**response.json())
        return model

    @allure.step("Обновление сущности")
    def patch_entity_by_id(self, entity_id, payload):
        response = requests.patch(
            url=self.endpoints.PATCH(entity_id),
            json=payload,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = EntityModel(**response.json())
        return model

    @allure.step("Удаление сущности")
    def delete_entity_by_id(self, entity_id):
        response = requests.delete(
            url=self.endpoints.DELETE(entity_id),
            headers=self.headers.basic,
        )
        assert response.status_code == 204, response.text
        self.attach_response(response.text)
        return response.status_code
