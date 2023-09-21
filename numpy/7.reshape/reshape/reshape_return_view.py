import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

reshaped_array = arr.reshape((4, 3))

print(f'arr : \n{arr}')
print(f'\nreshaped_array : \n{reshaped_array}')

# Set first row of reshaped_array to zero
reshaped_array[1, :] = 0

print(f'\narr : \n{arr}')
print(f'\nreshaped_array : \n{reshaped_array}')
