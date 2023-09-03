import numpy as np
import matplotlib.pyplot as plt

house_prices = [100000, 110000, 125000, 95000, 115000, 118000, 123000, 105000]

# Calculate the standard deviation of the data
mean = np.mean(house_prices)
variance = np.var(house_prices)
standard_deviation = np.sqrt(variance)

print(f'mean : {mean}')
print(f'variance : {variance}')
print(f'standard_deviation : {standard_deviation}')

# Create a scatter plot of data points
plt.scatter(house_prices, range(len(house_prices)), label='House prices', color='green', marker='o')

plt.axvline(standard_deviation, color='r', linestyle='dashed', linewidth=2, label=f'Standard Deviation: {standard_deviation:.2f}')
plt.axvline(mean, color='blue', linestyle='dashed', linewidth=2, label=f'Mean: {mean:.2f}')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.title('Scatter plot  with Variance')
plt.show()
