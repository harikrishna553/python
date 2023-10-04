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

# Get the dimensions of the binary array and kernel
input_image_height, input_image_width = binary_array.shape
kernel_height, kernel_width = kernel.shape
kernel_center = (kernel_height // 2, kernel_width // 2)

# Create an empty array to store the result of erosion
eroded_array = np.zeros_like(binary_array)

# Iterate through each pixel in the binary array
for i in range(input_image_height):
    for j in range(input_image_width):
        # Initialize the flag to check if all kernel elements match
        match_all = True

        # Check the overlapped region
        for m in range(kernel_height):
            for n in range(kernel_width):
                if kernel[m, n] == 1:
                    if (i + m - kernel_center[0] < 0 or i + m - kernel_center[0] >= input_image_height or
                        j + n - kernel_center[1] < 0 or j + n - kernel_center[1] >= input_image_width or
                        binary_array[i + m - kernel_center[0], j + n - kernel_center[1]] != 1):
                        match_all = False
                        break

        # If all kernel elements match, set the corresponding pixel in the eroded array to 1
        if match_all:
            eroded_array[i, j] = 1

# Print the original and eroded binary arrays
print("Original Binary Array:")
print(binary_array)

print("\nEroded Binary Array:")
print(eroded_array)