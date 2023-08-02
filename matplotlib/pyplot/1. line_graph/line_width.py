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

plt.plot(x1, y1, color='red', label='width-1.0', linestyle='-', marker='o', linewidth=1.0)
plt.plot(x2, y2, color='g', label='width-2.5', linestyle='--', marker='s', linewidth=2.5)
plt.plot(x3, y3, color='#0000FF', label='width-5.0', linestyle=':', marker='x', lw=5.0)
plt.plot(x4, y4, color=(0, 1, 1), label='width-7.5', linestyle='-.', marker='+', lw=7.5)

# To display the legend on the plot
plt.legend()

plt.show()
