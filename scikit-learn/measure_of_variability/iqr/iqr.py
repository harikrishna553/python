import numpy as np

data_points = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Calculate Q1
q1 = np.percentile(data_points, 25)

# Calculate Q3
q3 = np.percentile(data_points, 75)

# Calculate IQR
iqr = q3 - q1

print('Q1:', q1)
print('Q3:', q3)
print('IQR:', iqr)