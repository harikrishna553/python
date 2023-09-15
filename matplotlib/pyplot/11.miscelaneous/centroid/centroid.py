import matplotlib.pyplot as plt
import numpy as np

def rand_array(a, b, *more):
    return a + (b - a) * np.random.rand(*more)


# Generate some example data points
np.random.seed(47)

# Generate 100 rows, where each row has 2 columns and the values are in range of 1 and 10
min = 1
max = 10
data_points = rand_array(min, max, 100, 2)

# Define some default centroids for the two clusters
centroid1 = np.array([3, 6])
centroid2 = np.array([6, 8])

# Separate data points into two clusters based on distance from centroids
cluster1 = data_points[np.linalg.norm(data_points - centroid1, axis=1) < np.linalg.norm(data_points - centroid2, axis=1)]
cluster2 = data_points[np.linalg.norm(data_points - centroid2, axis=1) < np.linalg.norm(data_points - centroid1, axis=1)]

# Create a scatter plot of data points in cluster1 and cluster2
plt.scatter(cluster1[:, 0], cluster1[:, 1], c='blue', label='Cluster 1')
plt.scatter(cluster2[:, 0], cluster2[:, 1], c='red', label='Cluster 2')

# Plot the centroids
plt.scatter(centroid1[0], centroid1[1], c='blue', marker='x', s=100, label='Centroid 1')
plt.scatter(centroid2[0], centroid2[1], c='red', marker='x', s=100, label='Centroid 2')

# Add labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.title('Data Points and Centroids')

# Display the plot
plt.show()
