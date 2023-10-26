class Employee:
    total_employees = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.total_employees = Employee.total_employees + 1

    def attribute_check(self):
        if hasattr(self, 'name'):
            print('Employee has attribute name')

        if hasattr(self, 'age'):
            print('Employee has attribute age')

        if hasattr(self, 'total_employees'):
            print('Employee has attribute total_employees')

emp1 = Employee('Krishna', 35)
emp1.attribute_check()