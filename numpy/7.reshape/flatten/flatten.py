import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

flatten_array = arr.flatten()

print(f'arr : \n{arr}')
print(f'\nflatten_array : {flatten_array}')

print('\nSet the 3, 4 and 5th elements of flatten_array to 0')
flatten_array[3:6] = 0

print(f'\narr : \n{arr}')
print(f'\nflatten_array : {flatten_array}')