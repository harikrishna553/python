import numpy as np

# Create a NumPy array
arr = np.arange(1, 10)
print(f'arr : {arr}')

print('\nSet first five elements of slice to 0')

arr[:5] = 0
print(f'\narr : {arr}')