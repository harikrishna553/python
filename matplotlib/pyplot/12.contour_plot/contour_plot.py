import matplotlib.pyplot as plt
import numpy as np

# Create some data to plot
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2  # Example function to plot, you can replace this with your own data

# Create a filled contour plot
contour = plt.contourf(X, Y, Z,  alpha=0.4)  # cmap is the colormap for coloring the contour regions

# Add colorbar to show the scale of values
plt.colorbar(contour, label='Z Value')

# Add labels and a title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Filled Contour Plot')

# Show the plot
plt.show()
