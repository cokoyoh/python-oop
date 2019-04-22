import requests


class Employee:
    raise_amount = 1.05

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first_name.lower(), self.last_name.lower())

    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last_name}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'


employee_1 = Employee('John', 'Doe', 50000)
employee_2 = Employee('Jane', 'Doe', 67777)


# print(employee_1.first_name)
# print(employee_1.email)
# print(employee_1.fullname)
# del employee_1.fullname
# print(employee_1.fullname)