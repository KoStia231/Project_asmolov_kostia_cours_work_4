from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Salary:
    currency: str
    salary_to: int | None = None
    salary_from: int | None = None

    def __lt__(self, other):
        if None not in (self.salary_from, other.salary_from):
            if self.salary_from == other.salary_from:
                return self.salary_to < other.salary_to
            return self.salary_from < other.salary_from

        if self.salary_from is None and other.salary_from is None:
            return True

        if None in (self.salary_from, other.salary_from):
            return True

        return False


@dataclass(unsafe_hash=True)
class Vacancy:
    name: str
    url: str
    employer_name: str
    salary: Salary

    def __lt__(self, other):
        return self.salary < other.salary
