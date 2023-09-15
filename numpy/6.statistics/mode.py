import numpy as np
from scipy import stats

# Create a NumPy array
arr = np.array([1, 2, 2, 3, 4, 4, 5, 5, 5])

# Calculate the mode using scipy's stats.mode
mode_result = stats.mode(arr)

# The mode value is stored in mode_result.mode
mode_value = mode_result.mode
mode_count = mode_result.count

print(f"The mode is {mode_value} and it appears {mode_count} times.")
