import numpy as np

# Data points
data = np.array([100000, 120000, 150000, 170000, 200000, 700000, 200])

# Calculate the mean and standard deviation of the data
mean = np.mean(data)
std_dev = np.std(data)

# Calculate z-scores for each data point
z_scores = (data - mean) / std_dev

# Print the z-scores
print("Z-Scores:", z_scores)
