import numpy as np
from scipy.signal import convolve2d

# Define the input matrix (as a NumPy array)
input_matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 1],
    [2, 3, 4, 5, 6],
    [7, 8, 9, 1, 2]
])

# Define the kernel matrix (as a NumPy array)
kernel_matrix = np.array([
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1]
])

# Perform 2D convolution with different modes
convolution_valid = convolve2d(input_matrix, kernel_matrix, mode='valid')
convolution_full = convolve2d(input_matrix, kernel_matrix, mode='full')
convolution_same = convolve2d(input_matrix, kernel_matrix, mode='same')

# Print the convolution results for each mode
print(f'input_matrix : \n{input_matrix}')
print("\nConvolution (Valid Mode):\n", convolution_valid)
print("\nConvolution (Full Mode):\n", convolution_full)
print("\nConvolution (Same Mode):\n", convolution_same)
