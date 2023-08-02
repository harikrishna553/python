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

x5 = [8, 16, 24, 32, 40]
y5 = [25, 50, 75, 100, 125]

# Red color line
plt.plot(x1, y1, color='red', label='red-line')

# Green color line
plt.plot(x2, y2, color='g', label='green-line')

# Blue color line
plt.plot(x3, y3, color='#0000FF', label='blue-line')

# Aqua color line
plt.plot(x4, y4, color=(0, 1, 1), label='aqua-line')

# Red color line with opacity 0.5
plt.plot(x5, y5, color=(1, 0, 0, 0.5), label='red-line-opacity')

# Ti display the legend on the plot
plt.legend()

plt.show()
