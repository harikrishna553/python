import numpy as np
import matplotlib.pyplot as plt

arr = np.array([
    [2, 3],
    [4, 5],
    [1, 12],
    [6, 9],
    [5, 11],
    [3, 14],
    [8, 25]
    ]
)

centroid_x = np.mean(arr[:, 0])
centroid_y = np.mean(arr[:, 1])

print(f'centroid_x : {centroid_x}')
print(f'centroid_y : {centroid_y}')

plt.scatter(arr[:, 0], arr[:, 1], label='Data Points', c='red')

# Plot centroid
plt.scatter(centroid_x, centroid_y, c='blue', marker='x', s=100, label='Centroid')

plt.show()