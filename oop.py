class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name.lower() + '@example.com'
        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, programing_language):
        super().__init__(first_name, last_name, pay)
        self.programing_language = programing_language


class Manager(Employee):

    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)
        self.employees = employees

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def display_employees(self):
        for employee in self.employees:
            print('-->', employee.fullname())


developer_1 = Developer('John', 'Doe', 50000, 'Python')
developer_2 = Developer('Jane', 'Doe', 55000, 'Java')

manager_1 = Manager('Rick', 'Sanchez', 188000, [developer_1])

print(manager_1.email)
manager_1.add_employee(developer_2)
manager_1.remove_employee(developer_1)
manager_1.display_employees()