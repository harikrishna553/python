import matplotlib.pyplot as plt
import numpy as np

# Generate some example data points
np.random.seed(47)
data_points = np.random.randn(100, 2)  # 2D data points

# Assuming you have calculated centroids (C1 and C2) for two clusters
centroid1 = np.array([1, 1])
centroid2 = np.array([-1, -1])

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
