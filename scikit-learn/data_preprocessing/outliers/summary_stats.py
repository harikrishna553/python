import numpy as np

# Data points
data = np.array([100000, 120000, 150000, 170000, 200000, 700000, 200])

# Calculate summary statistics
mean = np.mean(data)             # Mean
median = np.median(data)         # Median
std_dev = np.std(data)           # Standard Deviation
variance = np.var(data)          # Variance
min_value = np.min(data)         # Minimum Value
max_value = np.max(data)         # Maximum Value
range_value = np.ptp(data)       # Range (Peak-to-Peak)

# Print the summary statistics
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Variance:", variance)
print("Minimum Value:", min_value)
print("Maximum Value:", max_value)
print("Range (Peak-to-Peak):", range_value)
