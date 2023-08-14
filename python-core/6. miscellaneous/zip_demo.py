ids = [1, 2, 3, 4]
names = ['Krishna', 'Narasimha', 'Ramesh', 'Sailu']
ages = [34, 39, 45, 35]
cities = ['Bangalore', 'Chennai', 'Bangalore', 'Hyderabad']

zipped = zip(ids, names, ages, cities)
print(zipped)

# iterating over the zipped object using for loop
print('\niterating over the zipped object using for loop')
for id, name, age, city in zipped:
    print(f'id : {id}, name : {name}, age : {age}, city : {city}')

# I can't iterate over a zipped object multiple times, so creating new one
zipped = zip(ids, names, ages, cities)
print('Convert the zipped object to a list')
list_of_tuples = list(zipped)
print(f'\nlist_of_tuples : \n{list_of_tuples}')

# I can't iterate over a zipped object multiple times, so creating new one
print('\nIterate over zipped object using next function')
zipped = zip(ids, names, ages, cities)
while True:
    try:
        id, name, age, city = next(zipped)
        print(f'id : {id}, name : {name}, age : {age}, city : {city}')
    except StopIteration:
        print('No more elements to process')
        break
