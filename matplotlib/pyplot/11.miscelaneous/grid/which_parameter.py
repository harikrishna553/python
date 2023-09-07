import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 100)
y = 10 * x + 123

plt.plot(x, y)

plt.minorticks_on()

# Customize major gridlines only
plt.grid(True, which='major', linestyle='--', color='red')

# Customize minor gridlines only
plt.grid(True, which='minor', linestyle=':', color='blue')

# Show the plot
plt.show()
