class Employee:
    def about_me(self):
        print('Employee Details')
        if hasattr(self, 'name'):
            print(f'name : {self.name}')
        if hasattr(self, 'age'):
            print(f'age : {self.age}')
        if hasattr(self, 'city'):
            print(f'city : {self.city}')
        print('')


emp1 = Employee()
emp1.name = 'Krishna'
emp1.age = 35

emp2 = Employee()
emp2.name = 'Ram'
emp2.age = 37
emp2.city= 'Bangalore'

# Print Employee details
emp1.about_me()
emp2.about_me()