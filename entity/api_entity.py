from typing import Optional

import allure
import requests

from config.headers import Headers
from utils.helper import Helper
from entity.endpoints import Endpoint
from entity.models.entity_model import EntityModel, EntityQueryModel


class EntityAPI(Helper):
    def __init__(self):
        super().__init__()
        self.endpoints = Endpoint()
        self.headers = Headers()

    @allure.step("Создание сущности")
    def create_entity(self, payload: EntityModel) -> EntityModel:
        response = requests.post(
            url=self.endpoints.CREATE,
            headers=self.headers.basic,
            json=payload.model_dump(exclude_none=True),
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())

        entity_id = response.json()  # это int

        # теперь получаем полноценный объект
        return self.get_entity_by_id(entity_id)

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
    def get_all_entity(self, query_params: Optional[EntityQueryModel] = None):
        response = requests.get(
            url=self.endpoints.GET_ALL,
            headers=self.headers.basic,
            params=query_params.model_dump(exclude_none=True) if query_params else None
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        return [
            EntityModel(**item)
            for item in response.json()["entity"]
        ]

    @allure.step("Обновление сущности")
    def patch_entity_by_id(self, entity_id, payload: EntityModel):
        response = requests.patch(
            url=self.endpoints.PATCH(entity_id),
            json=payload.model_dump(exclude_none=True),
            headers=self.headers.basic,
        )
        assert response.status_code == 204, response.text
        self.attach_response(f"Status code: {response.status_code}")

        return self.get_entity_by_id(entity_id)

    @allure.step("Удаление сущности")
    def delete_entity_by_id(self, entity_id):
        response = requests.delete(
            url=self.endpoints.DELETE(entity_id),
            headers=self.headers.basic,
        )
        assert response.status_code == 204, response.text
        self.attach_response(response.text)

        return response.status_code
