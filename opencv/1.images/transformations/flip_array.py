import numpy as np

# Create a sample 2D matrix (5x5)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Perform horizontal flip (left to right)
horizontal_flipped_matrix = np.flip(matrix, axis=1)

# Perform vertical flip (top to bottom)
vertical_flipped_matrix = np.flip(matrix, axis=0)

# Perform vertical flip (top to bottom)
horizontal_and_vertical_flipped_matrix = np.flip(matrix, axis=0)
horizontal_and_vertical_flipped_matrix = np.flip(horizontal_and_vertical_flipped_matrix, axis=1)

# Print the original, horizontally flipped, and vertically flipped matrices
print("Original Matrix:\n")
print(matrix)

print("\nHorizontally Flipped Matrix:\n")
print(horizontal_flipped_matrix)

print("\nVertically Flipped Matrix:\n")
print(vertical_flipped_matrix)

print("\nHorizontal and Vertical Flipped Matrix:\n")
print(horizontal_and_vertical_flipped_matrix)
