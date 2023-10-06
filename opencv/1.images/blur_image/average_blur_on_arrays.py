import numpy as np

# Define a sample 2D array (image) with pixel values
image = np.array([[1, 10, 10, 4, 5, 6],
                  [2, 10, 20, 20, 4, 70],
                  [3, 10, 20, 30, 4, 80],
                  [5, 10, 20, 30, 5, 90],
                  [5, 5, 90, 150, 0, 100],
                  [6, 70, 80, 90, 100, 5]])

# Define a 3x3 average blur kernel
kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]], dtype=float) / 9

# Create an empty result array of the same size as the image
result = np.zeros_like(image, dtype="uint8")

# Iterate through interior pixels (ignoring the corner rows and columns)
for i in range(1, image.shape[0] - 1):
    for j in range(1, image.shape[1] - 1):
        neighborhood = image[i-1:i+2, j-1:j+2]  # Extract the 3x3 neighborhood
        result[i, j] = np.sum(neighborhood * kernel)  # Apply the kernel

# Convert the result to integer values
result = np.round(result).astype(np.uint8)

# Print the original and blurred images
print("Original Image:")
print(image)
print("\nBlurred Image (Ignoring Corners):")
print(result)
