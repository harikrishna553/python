import numpy as np

array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Transpose the array
transposed_array = np.transpose(array, (2, 1, 0))

print(f'array : \n{array}')

# Print the transposed array
print(f'\ntransposed_array : \n{transposed_array}')