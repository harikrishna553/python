import numpy as np
import matplotlib.pyplot as plt

# Generate some random data with a mean of 0 and standard deviation of 1
house_prices = [100000, 110000, 125000, 95000, 115000, 118000, 123000, 105000]

# Calculate the standard deviation of the data
mean = np.mean(house_prices)
std_deviation = np.std(house_prices)

print(f'mean : {mean}')
print(f'std_deviation : {std_deviation}')

# Create a scatter plot of data points
plt.scatter(house_prices, range(len(house_prices)), label='House prices', color='green', marker='o')

plt.axvline(std_deviation, color='r', linestyle='dashed', linewidth=2, label=f'Standard Deviation: {std_deviation:.2f}')
plt.axvline(mean, color='blue', linestyle='dashed', linewidth=2, label=f'Mean: {mean:.2f}')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.title('Scatter plot  with Standard Deviation')
plt.show()
