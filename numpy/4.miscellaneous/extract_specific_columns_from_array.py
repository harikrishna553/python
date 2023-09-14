import numpy as np

arr1 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print(arr1)

# Extract first column
first_column = arr1[:,0]
second_column = arr1[:,1]
third_column = arr1[:,2]
fourth_column = arr1[:,3]

print(f'\nfirst_column : {first_column}')
print(f'\nsecond_column : {second_column}')
print(f'\nthird_column : {third_column}')
print(f'\nfourth_column : {fourth_column}')
