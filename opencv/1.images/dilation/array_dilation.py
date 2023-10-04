import numpy as np

# Create a binary array (0s and 1s)
binary_array = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0, 0]
], dtype=np.uint8)

# Create a square structuring element (kernel)
kernel = np.array([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
], dtype=np.uint8)

# Perform binary dilation using NumPy
dilated_array = np.zeros_like(binary_array)

# Get the dimensions of the binary array and kernel
input_array_height, input_array_width = binary_array.shape
kernel_height, kernel_width = kernel.shape
kernel_center = (kernel_height // 2, kernel_width // 2)

# Iterate through each pixel in the binary array
for i in range(input_array_height):
    for j in range(input_array_width):
        if binary_array[i, j] == 1:
            # Check the overlapped region
            for m in range(kernel_height):
                for n in range(kernel_width):
                    if i + m - kernel_center[0] >= 0 and i + m - kernel_center[0] < input_array_height and j + n - kernel_center[1] >= 0 and j + n - kernel_center[1] < input_array_width:
                        if kernel[m, n] == 1:
                            dilated_array[i + m - kernel_center[0], j + n - kernel_center[1]] = 1

# Print the original and dilated binary arrays
print("Original Binary Array:")
print(binary_array)

print("\nDilated Binary Array:")
print(dilated_array)