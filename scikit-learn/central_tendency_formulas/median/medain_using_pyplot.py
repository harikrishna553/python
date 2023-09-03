import matplotlib.pyplot as plt
import numpy as np

# Sample dataset
house_prices = [350000, 100000, 120000, 150000, 170000, 200000, 700000, 900000]

# Calculate the mean
mean = np.mean(house_prices)
median = np.median(house_prices)

# Create a scatter plot of data points
plt.scatter(house_prices, range(len(house_prices)), label='Data Points', color='blue', marker='o')

# Add a vertical line at the mean
plt.axvline(x=mean, color='red', linestyle='--', label='Mean')
plt.axvline(x=median, color='blue', linestyle='--', label='Median')

# Add labels and a title
plt.xlabel('House prices')
plt.ylabel('Index')
plt.title('Scatter Plot with Mean')

# Add a legend
plt.legend()

# Show the plot
plt.show()
