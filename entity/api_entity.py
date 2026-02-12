import allure
import requests

from config.headers import Headers
from utils.helper import Helper
from entity.payloads import Payload
from entity.endpoints import Endpoint
from entity.models.entity_model import EntityModel


class EntityAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = Payload()
        self.endpoints = Endpoint()
        self.headers = Headers()

    @allure.step("Создание сущности")
    def create_entity(self):
        response = requests.post(
            url=self.endpoints.CREATE,
            headers=self.headers.basic,
            json=self.payloads.create_entity,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = EntityModel(**response.json())
        return model

    @allure.step("Получение сущности по ID")
    def get_entity_by_id(self, id):
        response = requests.get(
            url=self.endpoints.GET_BY_ID(id),
            headers=self.headers.basic,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = EntityModel(**response.json())
        return model

    @allure.step("Получение списка сущностей")
    @allure.step("Обновление сущности")
    @allure.step("Удаление сущности")


