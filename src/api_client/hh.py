import requests

from .base import VacancyApiClient
from src.config.url import URL


class HeadHunterAPI(VacancyApiClient):

    def get_vacancies(self, search_text: str) -> list[dict]:
        url = URL
        params = {'only_with_salary': True, 'per_page': 100, 'text': search_text}

        responce = requests.get(url, params=params, timeout=10)
        if responce.status_code != 200:
            print(f"Ошибка {responce.content}")
            return []
        return responce.json()['items']
