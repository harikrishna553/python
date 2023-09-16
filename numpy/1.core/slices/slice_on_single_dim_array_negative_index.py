import numpy as np

# Create a NumPy array
arr = np.arange(1, 20)

# Slicing using negative indices
subset1 = arr[-3:]   # Last 3 elements: 17, 18, 19
subset2 = arr[-6:-2] # Elements from 6th to the 2nd last: [14 15 16 17]
subset3 = arr[:-4]   # All elements except the last 4: [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
subset4 = arr[-1::-1]  # Reverse the array: [19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1]

print(f'arr : {arr}')
print(f'subset1 : {subset1}')
print(f'subset2 : {subset2}')
print(f'subset3 : {subset3}')
print(f'subset4 : {subset4}')
