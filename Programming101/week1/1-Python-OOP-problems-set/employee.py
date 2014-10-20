class Employee(object):
    staff = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class HourlyEmployee(Employee):
    def __init__(self, name, hours):
        super().__init__(self, name)
        self.salary = salary


class SalariedEmployee(Employee):



class Manager(Employee):
