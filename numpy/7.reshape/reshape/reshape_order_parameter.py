import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

order_by_rows= arr.reshape((4, 3), order='C')
order_by_columns= arr.reshape((4, 3), order='F')

print(f'arr : \n{arr}')
print(f'\norder_by_rows : \n{order_by_rows}')
print(f'\norder_by_columns : \n{order_by_columns}')