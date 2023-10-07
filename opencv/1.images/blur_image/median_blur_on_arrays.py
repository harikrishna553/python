import numpy as np

# Create a sample 6x6 NumPy array
image = np.array([[5, 8, 7, 3, 2, 1],
                  [6, 9, 8, 4, 3, 2],
                  [4, 3, 2, 6, 7, 6],
                  [7, 8, 9, 5, 4, 3],
                  [5, 4, 5, 9, 9, 5],
                  [8, 7, 6, 7, 8, 4],
                  ], dtype=np.uint8)

# Define a function to apply median blur using a 3x3 kernel
def median_blur(input_image):
    output_image = np.zeros_like(input_image)

    for i in range(1, input_image.shape[0] - 1):
        for j in range(1, input_image.shape[1] - 1):
            # Extract the 3x3 neighborhood
            neighborhood = input_image[i - 1:i + 2, j - 1:j + 2]

            # Calculate the median of the neighborhood
            median_value = np.median(neighborhood)

            # Set the output pixel value to the median
            output_image[i, j] = median_value

    return output_image

# Apply median blur with a 3x3 kernel
median_blurred_image = median_blur(image)

print("Original Image:")
print(image)

print("\nMedian-Blurred Image:")
print(median_blurred_image)
