import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

flatten_array = np.ravel(arr)

print(f'arr : \n{arr}')
print(f'\nflatten_array : {flatten_array}')