import requests

from .base import VacancyApiClient
from src.config.url import URL
from ..dto import Vacancy, Salary


class HeadHunterAPI(VacancyApiClient):

    def get_vacancies(self, search_text: str) -> list[Vacancy]:
        url = URL
        params = {'only_with_salary': True, 'per_page': 100, 'text': search_text}

        response = requests.get(url, params=params, timeout=10)
        if response.status_code != 200:
            print(f"Ошибка\n"
                  f"{response.status_code}\n"
                  f"{response.content}")
            return []
        return [
            self._parse_vacancy(item) for item in response.json()['items']
        ]

    def _parse_vacancy(self, data: dict) -> Vacancy:
        return Vacancy(
            name=data['name'],
            url=data['alternate_url'],
            employer_name=data['employer']['name'],
            salary=Salary(salary_from=data['salary']['from'],
                          salary_to=data['salary']['to'],
                          currency=data['salary']['currency'])
        )
