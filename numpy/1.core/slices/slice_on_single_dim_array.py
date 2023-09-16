import numpy as np

# Create a NumPy array
arr = np.arange(1, 20)

# Slicing to get a subset of the array
subset1 = arr[2:6]  # Elements at index 2, 3, 4, 5
subset2 = arr[:5]   # Elements at index 0, 1, 2, 3, 4
subset3 = arr[::2]  # Every second element: 0, 2, 4, 6, 8
subset4 = arr[1::2]  # Every second element starting from index 1: 1, 3, 5, 7, 9
subset5 = arr[:5:] # Elements at index 0, 1, 2, 3, 4

print(f'arr : {arr}')
print(f'subset1 : {subset1}') # Output: [3 4 5 6]
print(f'subset2 : {subset2}') # Output: [1 2 3 4 5]
print(f'subset3 : {subset3}') # Output: [ 1  3  5  7  9 11 13 15 17 19]
print(f'subset4 : {subset4}') # Output: [ 2  4  6  8 10 12 14 16 18]
print(f'subset5 : {subset5}') # Output: [1 2 3 4 5]
