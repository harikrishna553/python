import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10)
y = 10 * x + 123

plt.plot(x, y)

plt.minorticks_on()

# Show the plot
plt.show()
