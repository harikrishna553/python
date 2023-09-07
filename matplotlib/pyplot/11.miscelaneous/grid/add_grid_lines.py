import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10)
y = 10 * x + 123

plt.plot(x, y, label='y = 10 * x + 123')

plt.grid(True)
plt.show()