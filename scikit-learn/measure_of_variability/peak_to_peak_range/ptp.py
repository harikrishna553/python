import matplotlib.pyplot as plt
import numpy as np

# Generate some random data with a mean of 0 and standard deviation of 1
house_prices = [100000, 110000, 125000, 95000, 115000, 118000, 123000, 105000]

max_value = np.max(house_prices)
min_value = np.min(house_prices)

# Range (Peak-to-Peak)
range_value = np.ptp(house_prices)

print(f'max_value : {max_value}')
print(f'min_value : {min_value}')
print(f'range_value : {max_value-min_value}')
print(f'range_value : {range_value}')

# Create a histogram to visualize the data
plt.hist(house_prices, bins=10, edgecolor='k', alpha=0.7)
plt.axvline(min_value, color='red', linestyle='--', label=f'Min: {min_value}')
plt.axvline(max_value, color='blue', linestyle='--', label=f'Max: {max_value}')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title(f'Peak-to-Peak Range: {range_value}')

# Add legend
plt.legend()

# Show the plot
plt.show()