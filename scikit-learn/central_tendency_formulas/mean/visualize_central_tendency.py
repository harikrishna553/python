import matplotlib.pyplot as plt
import numpy as np

# Sample dataset
data = [10, 20, 30, 40, 50, 60]

# Calculate the mean
mean = np.mean(data)

# Create a scatter plot of data points
plt.scatter(data, range(len(data)), label='Data Points', color='blue', marker='o')

# Add a vertical line at the mean
plt.axvline(x=mean, color='red', linestyle='--', label='Mean')

# Add labels and a title
plt.xlabel('Actual value')
plt.ylabel('Index')
plt.title('Scatter Plot with Mean')

# Add a legend
plt.legend()

# Show the plot
plt.show()
