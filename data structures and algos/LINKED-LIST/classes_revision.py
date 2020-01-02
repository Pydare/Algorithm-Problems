class Employee:

    raise_amount = 1.04
    num_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_emp += 1

    def fullname(self):
        return f'The full name of employee is {self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())


emp1 = Employee('Dare', 'Adewumi', 50000)
emp2 = Employee('Seyi', 'Adewumi', 60000)

dev1 = Developer('Dare', 'Adewumi', 110000, 'python')
dev2 = Developer('Seyi', 'Adewumi', 100000, 'java')

mgr1 = Manager('Sue', 'Smith', 150000, [dev1])



mgr1.add_emp(dev2)
print(mgr1.print_emps())
dev1.apply_raise()
print(dev1.pay)

# import datetime
# my_date = datetime.date(2016, 7, 10)

# print(Employee.is_workday(my_date))




