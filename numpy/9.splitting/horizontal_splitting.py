import numpy as np

# Create employee records with (id, name, age and city
original_array = np.array([[1, 'Krishna', 37, 'Bangalore'],
                            [2, 'Gopi', 38, 'Hyderabad'],
                            [3, 'Chamu', 34, 'Chennai']])

print('Split the array into two equal parts  along columns')
# Split the array into two equal parts  along columns
# part 1 : (id, name) and
# part 2 : (age, city)
subarrays = np.hsplit(original_array, 2)

print(f'subarrays[0] : \n{subarrays[0]}')
print(f'\nsubarrays[1] : \n{subarrays[1]}')

print('Split the array into three parts  along columns')
# Split the array into three parts  along columns
# part 1 : (id, name) and
# part 2 : (age)
# part 3 : (city)
subarrays = np.hsplit(original_array, [2, 3, 4])
print(f'\nsubarrays[0] : \n{subarrays[0]}')
print(f'\nsubarrays[1] : \n{subarrays[1]}')
print(f'subarrays[1] : \n{subarrays[2]}')


