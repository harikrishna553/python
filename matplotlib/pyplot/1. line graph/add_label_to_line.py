import matplotlib.pyplot as plt
import numpy as np

# Sample data
x1 = [5, 10, 15, 20, 25]
y1 = [20, 40, 60, 80, 100]

x2 = [10, 20, 30, 40, 50]
y2 = [30, 60, 90, 120, 150]

# Red color line
plt.plot(x1, y1, color='red', label='red-line')

# Green color line
plt.plot(x2, y2, color='g', label='green-line')

# Ti display the legend on the plot
plt.legend()

plt.show()
