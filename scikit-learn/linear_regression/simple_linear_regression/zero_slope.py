import matplotlib.pyplot as plt
import numpy as np

# Define the equation parameters
m = 0  # Slope
c = 10  # Y-intercept

# Generate x values
x = np.arange(-100, 100)

# Calculate corresponding y values
y = (m * x) + c

# Create the plot
plt.plot(x, y, label=f'y = {m}x + {c}')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Graph of y = {m}x + {c}')
plt.grid(True)
plt.legend()
plt.show()
