class Employee:
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name.lower() + '@example.com'

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first_name, self.last_name, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


employee_1 = Employee('John', 'Doe', 50000)
employee_2 = Employee('Jane', 'Doe', 69888)

print(len(employee_2))
# print(employee_1 + employee_2)
# print(employee_1)
# print(repr(employee_1))
# print(str(employee_1))
