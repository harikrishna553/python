import numpy as np

# Create employee records with (id, name, age and city
original_array = np.array([[1, 'Krishna', 37, 'Bangalore'],
                            [2, 'Gopi', 38, 'Hyderabad'],
                            [3, 'Chamu', 34, 'Chennai'],
                            [4, 'Narasimha', 36, 'Chennai'],
                            [5, 'Pulak', 39, 'Bangalore'],
                            [6, 'Raj', 31, 'Bangalore']])

print('Split the array into three equal parts along rows')
# Split the array into three equal parts  along columns
subarrays = np.vsplit(original_array, 3)

print(f'subarrays[0] : \n{subarrays[0]}')
print(f'\nsubarrays[1] : \n{subarrays[1]}')
print(f'\nsubarrays[2] : \n{subarrays[2]}')

print('\nSplit the array into three parts along rows')
# Split the array into three parts  along columns
subarrays = np.vsplit(original_array, [2, 3, 7])
print(f'\nsubarrays[0] : \n{subarrays[0]}')
print(f'\nsubarrays[1] : \n{subarrays[1]}')
print(f'\nsubarrays[2] : \n{subarrays[2]}')


