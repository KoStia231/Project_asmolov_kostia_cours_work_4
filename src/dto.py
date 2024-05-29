from dataclasses import dataclass


@dataclass
class Salary:
    currency: str
    salary_to: int | None = None
    salary_from: int | None = None


@dataclass
class Vacancy:
    name: str
    url: str
    employer_name: str
    salary: Salary

    def __lt__(self, other):
        return self.salary < other.salary
