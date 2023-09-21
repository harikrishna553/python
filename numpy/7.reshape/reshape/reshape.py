import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

four_rows_three_columns= arr.reshape((4, 3))
six_rows_two_columns= arr.reshape((6, 2))

print(f'arr : \n{arr}')
print(f'\nfour_rows_three_columns : \n{four_rows_three_columns}')
print(f'\nsix_rows_two_columns : \n{six_rows_two_columns}')