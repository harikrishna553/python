import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([1.0, 2.34, 7.89])
arr3 = np.array(['a', 'b'])

# Print size of the array
print('Type of arr1 : ', arr1.dtype)
print('Size of arr1 is : ', arr1.itemsize, ' bytes')

print('\nType of arr2 : ', arr2.dtype)
print('Size of arr2 is : ', arr2.itemsize, ' bytes')

print('\nType of arr3 : ', arr3.dtype)
print('Size of arr3 is : ', arr3.itemsize, ' bytes')