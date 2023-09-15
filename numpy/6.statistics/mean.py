import numpy as np

arr1 = np.array([2, 3, 5, 7])
average_of_values = np.mean(arr1)

print(f'arr1 : {arr1}\n')
print(f'average_of_values : {average_of_values}\n')

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 2, 3]
])
average_along_columns = np.mean(arr2, axis=0)
average_along_rows = np.mean(arr2, axis=1)

print(f'\narr2 : {arr2}\n')
print(f'average_along_columns : {average_along_columns}\n')
print(f'average_along_rows : {average_along_rows}\n')
