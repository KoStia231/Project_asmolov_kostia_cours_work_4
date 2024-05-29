from abc import ABC, abstractmethod

from src.dto import Vacancy


class BaseConnector(ABC):
    @abstractmethod
    def get_vacancies(self) -> list[Vacancy]:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def del_vacancy(self, vacancy: Vacancy) -> None:
        pass
