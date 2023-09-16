import numpy as np

arr1 = np.array([1.5, 2.6, 3, 4, 5], dtype='int32')
arr2 = np.array([1, 2, 3.9, 4, 5], dtype='float64')

print(f'arr1 : {arr1}')
print(f'arr1 element type : {arr1.dtype}')
print(f'arr1 element size : {arr1.itemsize}')

print(f'\narr2 : {arr2}')
print(f'arr2 element type : {arr2.dtype}')
print(f'arr2 element size : {arr2.itemsize}')