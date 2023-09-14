import matplotlib.pyplot as plt
import numpy as np

# Define the vertices of the triangle
vertices = np.array([
    [0, 0],
    [4, 0],
    [2, 3]
])

# Calculate the centroid of the triangle
centroid = np.mean(vertices, axis=0)

# Create a scatter plot of the triangle vertices
plt.scatter(vertices[:, 0], vertices[:, 1], c='blue', marker='o', label='Vertices')

# Plot the centroid
plt.scatter(centroid[0], centroid[1], c='red', marker='x', s=150, label='Centroid')

# Add labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.title('Triangle with Centroid')

# Connect the vertices to form the triangle
triangle = plt.Polygon(vertices, closed=True, fill=None,  color='blue')
plt.gca().add_patch(triangle)

# Display the plot
plt.show()
