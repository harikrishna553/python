# Define a simple class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of the Person class
person1 = Person("Alice", 30)
person2 = Person("Ram", 35)

# Print the initial attributes
print(f'Initial attributes - {person1.__dict__}')
print(f'Initial attributes - {person2.__dict__}')

# Dynamically add a new attribute to the object
person1.country = "USA"
person2.hobbies = ['Cricket', 'Chess']

# Print the updated attributes
print(f'After updation - {person1.__dict__}')
print(f'After updation - {person2.__dict__}')
