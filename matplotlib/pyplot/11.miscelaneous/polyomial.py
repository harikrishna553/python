import matplotlib.pyplot as plt
import numpy as np

# Create a figure with a specific size (width, height)
plt.figure(figsize=(12, 10))

# Define the vertices of the triangle
triangle_vertices = np.array([
    [0, 0],
    [4, 0],
    [2, 3]
])
# Create a scatter plot of the triangle vertices
plt.scatter(triangle_vertices[:, 0], triangle_vertices[:, 1], c='blue', marker='o', label='Triangle')
# Connect the vertices to form the triangle
triangle = plt.Polygon(triangle_vertices, closed=True, fill=True, color='blue', alpha=0.5)
plt.gca().add_patch(triangle)

# Define the vertices of the Square
square_vertices = np.array([
    [5, 0],
    [5, 5],
    [10, 5],
    [10, 0]
])
# Create a scatter plot of the triangle vertices
plt.scatter(square_vertices[:, 0], square_vertices[:, 1], c='green', marker='o', label='Square')
square = plt.Polygon(square_vertices, closed=True, fill=None, color='green', linestyle='--')
plt.gca().add_patch(square)


pentagon_vertices = np.array([
    [1, 5],
    [1, 7],
    [3, 7],
    [3, 4],
    [2, 4]
])
# Create a scatter plot of the triangle vertices
plt.scatter(pentagon_vertices[:, 0], pentagon_vertices[:, 1], c='red', marker='o', label='Pentagon')
pentagon = plt.Polygon(pentagon_vertices, closed=False, fill=False, color='green')
plt.gca().add_patch(pentagon)

# Add labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.title('Polygon')
plt.xticks(np.arange(1, 10))
plt.yticks(np.arange(1, 10))

# Display the plot
plt.show()
