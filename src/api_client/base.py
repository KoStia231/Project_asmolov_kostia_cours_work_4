from abc import ABC, abstractmethod


class VacancyApiClient(ABC):

    @abstractmethod
    def get_vacancies(self, search_text: str) -> list[dict]:
        pass
