from src.api_client.hh import HeadHunterAPI


def main():
    client = HeadHunterAPI()
    vacancy = client.get_vacancies('python')
    for vacancy in vacancy:
        print(vacancy)
    print("Hello")


if __name__ == "__main__":
    main()
