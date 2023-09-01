import numpy as np

# Sample data with outliers
data = np.array( [27, 98, 123, 4, 6, 897, 643])

# Calculate the median and IQR
median = np.median(data)
iqr = np.percentile(data, 75) - np.percentile(data, 25)

# Apply robust scaling
robust_scaled_data = (data - median) / iqr

# Print the robust-scaled data
print("Robust Scaled Data:")
print(robust_scaled_data)
