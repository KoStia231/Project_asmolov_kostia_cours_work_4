from src.dto import Salary


class TestSalaryCompare:

    def test_salary(self):
        salary_1 = Salary(salary_from=None, salary_to=None, currency='USD')
        salary_2 = Salary(salary_from=None, salary_to=None, currency='USD')

        assert salary_1 == salary_2

    def test_salary_1(self):
        salary_1 = Salary(salary_from=100, salary_to=200, currency='USD')
        salary_2 = Salary(salary_from=100, salary_to=200, currency='USD')

        assert salary_1 == salary_2

