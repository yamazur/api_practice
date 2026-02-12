import allure
import json
from allure_commons.types import AttachmentType

class Helper: #данный метод позволяет прикрепить красивый json к отчету

    def attach_response(self, response):
        response = json.dumps(response, indent=4) #dumps преобразует питон-объект в json-строку
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)