from pathlib import Path

from src.api_client.base import VacancyApiClient
from src.api_client.hh import HeadHunterAPI
from src.connector.base import BaseConnector
from src.connector.connector_json import ConnectorJson
from src.interactive.interactive import START_MASSAGE

BASE_PATH = Path(__file__).parent
VACANCIES_PATH_FILE = BASE_PATH.joinpath("vacancies.json")
client: VacancyApiClient = HeadHunterAPI()
connector_json: BaseConnector = ConnectorJson(VACANCIES_PATH_FILE)


def user_choice_1():
    search_word = input('Ключевое слово:\n')
    vacancies = client.get_vacancies(search_word.lower())
    for vacancy in vacancies:
        connector_json.add_vacancy(vacancy)


def user_choice_2():
    n_vacancies = int(input('\nСколько вакансий вывести?\n'))
    vacancies = connector_json.get_vacancies()
    print(f'\nВот {n_vacancies} вакансий с сортировкой по зарплате\n')
    for vacancy in sorted(vacancies, key=lambda x: x.salary, reverse=True)[:n_vacancies]:
        print('*' * 70)
        print(vacancy)


def user_choice_3():
    vacancies = connector_json.get_vacancies()
    for vacancy in vacancies:
        connector_json.del_vacancy(vacancy)


def main():
    while True:
        print(START_MASSAGE)
        user_input = input()
        if not user_input.isdigit():
            continue

        user_choice = int(user_input)
        if user_choice == 0:
            break

        elif user_choice == 1:
            user_choice_1()

        elif user_choice == 2:
            user_choice_2()

        elif user_choice == 3:
            user_choice_3()


if __name__ == "__main__":
    main()
