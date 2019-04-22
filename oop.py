class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name.lower() + '@example.com'

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)


employee_1 = Employee('John', 'Doe')
employee_2 = Employee('Jane', 'Doe')

