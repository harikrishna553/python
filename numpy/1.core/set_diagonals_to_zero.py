import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(f'arr: \n{arr}')

#arr[[0, 1, 2], [0, 1, 2]] = 0

# Assume array is of nXn size
n = arr.shape[0]
arr[range(n), range(n)] = 0

print(f'\narr: \n{arr}')