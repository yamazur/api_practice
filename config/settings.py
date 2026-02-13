import os #чтобы читать системные настройки
from dotenv import load_dotenv #чтобы читать .env файл

load_dotenv() # читаем файл .env и загружаем переменные

class Settings:
    BASE_URL = os.getenv("BASE_URL", "http://localhost:8080") # читаем из .env файла, если нет - используем "http://localhost:8080"
    API_PREFIX = "/api" #'то общая "папка", где лежат все  API endpoints
    API_URL = f"{BASE_URL}{API_PREFIX}"
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    REQUEST_TIMEOUT = 15

config = Settings()
