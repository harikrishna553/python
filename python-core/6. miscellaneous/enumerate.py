# Iterate over a list
print('\nIterate over a list')
primes = [2, 3, 5, 7, 11]
for index, value in enumerate(primes):
    print(f'index : {index}, value : {value}')

# Iterate over a tuple
print('\nIterate over a tuple')
employee = (1, 'Krishna', 34, 'Bangalore')
for index, value in enumerate(employee):
    print(f'index : {index}, value : {value}')

# Iterate over a string
print('\nIterate over a string')
str = 'aeiou'
for index, value in enumerate(str):
    print(f'index : {index}, value : {value}')

# Iterate over a string from starting and index position at 2
print('\nIterate over a string from starting and index position at 2')
str = 'aeiou'
for index, value in enumerate(str, start=2):
    print(f'index : {index}, value : {value}')