import os #чтобы читать системные настройки
from dotenv import load_dotenv #чтобы читать .env файл

load_dotenv() # читаем файл .env и загружаем переменные

class Settings:
    BASE_URL = os.getenv("BASE_URL", "http://localhost:8080") # читаем из .env файла, если нет - используем "http://localhost:8080"
    API_PREFIX = "/api" #'то общая "папка", где лежат все  API endpoints
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    REQUEST_TIMEOUT = 5

    @property
    def api_url(self):
        return f"{self.BASE_URL}{self.API_PREFIX}"

config = Settings()
