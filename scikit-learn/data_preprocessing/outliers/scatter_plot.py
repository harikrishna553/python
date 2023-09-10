import numpy as np
import matplotlib.pyplot as plt

# Sample house prices
house_prices = np.array([100000, 120000, 150000, 170000, 200000, 700000, 200])

# Create an array for x-axis values (e.g., index or house number)
x_values = np.arange(1, len(house_prices) + 1)

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x_values, house_prices, color='blue', label='House Prices')

plt.xlabel('House Number')
plt.ylabel('House Price (in USD)')
plt.title('House Prices Scatter Plot')
plt.grid(True)

plt.legend()
plt.show()
