class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return '{}.{}@example.com'.format(self.first_name.lower(), self.last_name.lower())

    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @fullname.setter
    def fullname(self, fullname):
        first_name, last_name = fullname.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    @fullname.deleter
    def fullname(self):
        print('Deleting name!')
        self.first_name = None
        self.last_name = None


employee_1 = Employee('John', 'Doe')
employee_2 = Employee('Jane', 'Doe')

employee_1.fullname = 'Richard Roe'

print(employee_1.first_name)
print(employee_1.email)
print(employee_1.fullname)
del employee_1.fullname
print(employee_1.fullname)