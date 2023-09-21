import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
transposed_array = arr.transpose((1, 0))

print(f'arr : \n{arr}')
print(f'\ntransposed_array : \n{transposed_array}')