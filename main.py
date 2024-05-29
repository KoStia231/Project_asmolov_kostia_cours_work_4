from pathlib import Path

from src.api_client.base import VacancyApiClient
from src.api_client.hh import HeadHunterAPI
from src.connector.base import BaseConnector
from src.connector.connector_json import ConnectorJson

BASE_PATH = Path(__file__).parent
VACANCIES_PATH_FILE = BASE_PATH.joinpath("vacancies.json")
client: VacancyApiClient = HeadHunterAPI()
connector_json: BaseConnector = ConnectorJson(VACANCIES_PATH_FILE)


def main():

    vacancies = client.get_vacancies('python')
    for vacancy in vacancies:
        print(vacancy)

        connector_json.add_vacancy(vacancy)


if __name__ == "__main__":
    main()
