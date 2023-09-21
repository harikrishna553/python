import numpy as np

ids = np.array([1, 2, 3])
names = np.array(['Krishna', 'Chamu', 'Gopi'])
ages = np.array([36, 33, 37])
cities = np.array(['Bangalore', 'Chennai', 'Hyderabad'])

emps = np.column_stack((ids, names, ages, cities))

print(f'emps : \n{emps}')