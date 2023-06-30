import numpy as np

# One dimensional array
arr1 = np.array([2, 3, 5, 7])

print('Shape of the arr1 : ', arr1.shape)
print('arr1[0] : ', arr1[0])
print('arr1[1] : ', arr1[1])
print('arr1[2] : ', arr1[2])
print('arr1[3] : ', arr1[3])

# Two dimensional array
arr2 = np.array([
    [2, 3, 5, 7],
    [11, 13, 17, 19]
])
print('\nShape of the arr2 : ', arr2.shape)

# Access two dimensional array elements
print('arr2[0][2] : ', arr2[0][2])
print('arr2[1][3] : ', arr2[1][2])

print('arr2[0, 2] : ', arr2[0, 2])
print('arr2[0, 2] : ', arr2[1, 2])