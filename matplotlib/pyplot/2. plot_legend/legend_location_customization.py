import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10)
y1 = x**2
y2 = x**3

plt.plot(x, y1, label="y = x^2", color='r')
plt.plot(x, y2, label="y = x^3", color='g')

plt.legend(loc='upper left')
plt.show()