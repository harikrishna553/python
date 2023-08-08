import matplotlib.pyplot as plt
import numpy as np

# Sample data
x1 = [5, 10, 15, 20, 25]
y1 = [20, 40, 60, 80, 100]

x2 = [10, 20, 30, 40, 50]
y2 = [30, 60, 90, 120, 150]

x3 = [15, 30, 45, 60, 75]
y3 = [8, 16, 24, 32, 40]

x4 = [12, 24, 36, 48, 60]
y4 = [15, 30, 45, 60, 75]

# Create a new figure with a specific size
plt.figure(figsize=(8, 6))

plt.plot(x1, y1, color='red', label='markersize-5', linestyle='-', marker='o', markersize=5)
plt.plot(x2, y2, color='g', label='markersize-10', linestyle='--', marker='o', markersize=10)
plt.plot(x3, y3, color='#0000FF', label='markersize-15', linestyle=':', marker='o', markersize=15)
plt.plot(x4, y4, color=(0, 1, 1), label='markersize-20', linestyle='-.', marker='o', markersize=20)

# To display the legend on the plot
plt.legend(fontsize=12)

plt.show()
