import matplotlib.pyplot as plt
import numpy as np

# Define the center and radius of the circle
center = (3, 3)  # Center coordinates (x, y)
radius = 2

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the circle
circle = plt.Circle(center, radius, fill=False, color='blue')
ax.add_patch(circle)

# Plot the center
plt.scatter(center[0], center[1], c='red', marker='o', s=100, label='Centroid')

plt.legend()
plt.title('Circle with Center')

# Set axis limits for a better view
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

plt.show()
