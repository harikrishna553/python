import matplotlib.pyplot as plt
import numpy as np

# Sample data
x1 = [5, 10, 15, 20, 25, 30, 35, 40, 45]
y1 = [ 70, 235, 500, 865, 1330, 1895, 2560, 3325, 4190]

plt.plot(x1[:4], y1[:4], linestyle='-', color='b')
plt.plot(x1[3:], y1[3:], linestyle='--', color='r')

# To display the legend on the plot
plt.legend()

plt.title('solid and dashed line mix')

plt.show()
