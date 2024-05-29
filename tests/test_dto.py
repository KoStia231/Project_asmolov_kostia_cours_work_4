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

    def test_salary_2(self):
        salary_1 = Salary(salary_from=100, salary_to=None, currency='USD')
        salary_2 = Salary(salary_from=200, salary_to=None, currency='USD')

        assert salary_1.salary_from < salary_2.salary_from

    def test_salary_3(self):
        salary_1 = Salary(salary_from=200, salary_to=None, currency='USD')
        salary_2 = Salary(salary_from=100, salary_to=None, currency='USD')

        assert salary_1.salary_from > salary_2.salary_from

    def test_salary_4(self):
        salary_1 = Salary(salary_from=None, salary_to=100, currency='USD')
        salary_2 = Salary(salary_from=None, salary_to=200, currency='USD')

        assert salary_1.salary_to < salary_2.salary_to

    def test_salary_5(self):
        salary_1 = Salary(salary_from=None, salary_to=200, currency='USD')
        salary_2 = Salary(salary_from=None, salary_to=100, currency='USD')

        assert salary_1.salary_to > salary_2.salary_to

