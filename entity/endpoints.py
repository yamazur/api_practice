from config.settings import config

HOST = config.API_URL  # http://localhost:8080/api

class Endpoint:

    # статические эндпоинты
    CREATE = f"{HOST}/create"  # POST
    GET_ALL = f"{HOST}/getAll"  # GET

    # динамические эндпоинты
    GET_BY_ID = lambda self, id: f"{HOST}/get/{id}"  # GET
    PATCH = lambda self, id: f"{HOST}/patch/{id}"  # PATCH
    DELETE = lambda self, id: f"{HOST}/delete/{id}"  # DELETE