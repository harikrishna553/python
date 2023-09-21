import numpy as np

# Create two sample 2D arrays
arr1 = np.array([[1, 2],
                   [3, 4]])

arr2 = np.array([[5, 6],
                   [7, 8]])

# Depth stack the arrays
result = np.dstack((arr1, arr2))

print(f'arr1 : \n{arr1}')
print(f'\narr2 : \n{arr2}')
print(f'\nresult : \n{result}')
