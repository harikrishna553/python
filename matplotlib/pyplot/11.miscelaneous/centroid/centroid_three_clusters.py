import matplotlib.pyplot as plt
import numpy as np

def rand_array(a, b, *more):
    return a + (b - a) * np.random.rand(*more)

# Generate some example data points
np.random.seed(47)

# Generate 100 rows, where each row has 2 columns and the values are in the range of 1 and 10
min_val = 1
max_val = 10
data_points = rand_array(min_val, max_val, 100, 2)

# Define centroids for the three clusters
centroid1 = np.array([3, 6])
centroid2 = np.array([6, 8])
centroid3 = np.array([4, 4])  # New centroid for the third cluster

# Calculate distances from each data point to all three centroids
distances = np.column_stack([
    np.linalg.norm(data_points - centroid1, axis=1),
    np.linalg.norm(data_points - centroid2, axis=1),
    np.linalg.norm(data_points - centroid3, axis=1)
])

# Determine the cluster assignment for each data point based on the closest centroid
cluster_assignment = np.argmin(distances, axis=1)

# Separate data points into three clusters based on cluster assignment
cluster1 = data_points[cluster_assignment == 0]
cluster2 = data_points[cluster_assignment == 1]
cluster3 = data_points[cluster_assignment == 2]

# Create a scatter plot of data points in all three clusters
plt.scatter(cluster1[:, 0], cluster1[:, 1], c='blue', label='Cluster 1')
plt.scatter(cluster2[:, 0], cluster2[:, 1], c='red', label='Cluster 2')
plt.scatter(cluster3[:, 0], cluster3[:, 1], c='green', label='Cluster 3')

# Plot the centroids
plt.scatter(centroid1[0], centroid1[1], c='blue', marker='x', s=100, label='Centroid 1')
plt.scatter(centroid2[0], centroid2[1], c='red', marker='x', s=100, label='Centroid 2')
plt.scatter(centroid3[0], centroid3[1], c='green', marker='x', s=100, label='Centroid 3')

# Add labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.title('Data Points and Centroids for 3 Clusters')

# Display the plot
plt.show()
