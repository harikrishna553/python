import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(f'arr : \n{arr}')
arr.resize((4, 3))

print('\nAfter resizing to 4 rows and 3 columns')
print(f'arr : \n{arr}')
