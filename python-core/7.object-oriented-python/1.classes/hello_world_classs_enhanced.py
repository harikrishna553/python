class Employee:

    def __init__(self, name, age, city='Bangalore'):
        print(f'New object is getting created')
        self.name = name
        self.age = age
        self.city = city

    def about_me(self):
        print('Employee Details')
        print(f'name : {self.name}')
        print(f'age : {self.age}')
        print(f'city : {self.city}')
        print('')

emp1 = Employee('Krishna', 35)
emp2 = Employee('Ram', 37, 'Hyderabad')

# Print Employee details
emp1.about_me()
emp2.about_me()