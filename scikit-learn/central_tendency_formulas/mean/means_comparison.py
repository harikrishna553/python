import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gmean
from scipy import stats

# Sample dataset
data = np.array([20, 400, 32, 456, 98, 500, 23, 45, 235])
# Sample weights
weights = np.array([2, 4, 2, 4, 2, 4, 3, 4, 3])

# Calculate the mean
arithmetic_mean = np.mean(data)
# Calculate the weighted mean
weighted_mean = np.average(data, weights=weights)
# Calculate the geometric mean
geometric_mean = gmean(data)
# Calculate the harmonic mean manually
harmonic_mean = len(data) / np.sum(1.0 / data)
# Calculate the quadratic mean manually
quadratic_mean = np.sqrt(np.mean(data ** 2))
# Calculate the trimmed mean by trimming 10% from both ends
trimmed_mean = stats.trim_mean(data, proportiontocut=0.20)

# Create a scatter plot of data points
plt.scatter(data, range(len(data)), label='Data Points', color='blue', marker='o')

# Add a vertical line at the mean
plt.axvline(x=arithmetic_mean, color='red', label='Arithmetic Mean')
plt.axvline(x=weighted_mean, color='magenta', label='Weighted Mean')
plt.axvline(x=geometric_mean, color='yellow', label='Geometric Mean')
plt.axvline(x=harmonic_mean, color='black', label='Harmonic Mean')
plt.axvline(x=quadratic_mean, color='cyan', label='Quadratic Mean')
plt.axvline(x=trimmed_mean, color='blue', label='Trimmed Mean')

# Add labels and a title
plt.xlabel('Actual value')
plt.ylabel('Index')
plt.title('Scatter Plot with Mean')

# Add a legend
plt.legend()

# Show the plot
plt.show()

print(f'arithmetic_mean : {arithmetic_mean}')
print(f'weighted_mean : {weighted_mean}')
print(f'geometric_mean : {geometric_mean}')
print(f'harmonic_mean : {harmonic_mean}')
print(f'quadratic_mean : {quadratic_mean}')
print(f'trimmed_mean : {trimmed_mean}')

