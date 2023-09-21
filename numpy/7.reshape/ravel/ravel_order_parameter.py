import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

flatten_array_row_wise = np.ravel(arr, order='C')
flatten_array_column_wise = np.ravel(arr, order='F')

print(f'arr : \n{arr}')
print(f'\nflatten_array_row_wise : {flatten_array_row_wise}')
print(f'\nflatten_array_column_wise : {flatten_array_column_wise}')