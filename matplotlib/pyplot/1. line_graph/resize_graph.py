import matplotlib.pyplot as plt
import numpy as np

# Sample data
x1 = [5, 10, 15, 20, 25]
y1 = [20, 40, 60, 80, 100]

plt.figure(figsize=(5, 3), dpi=300)
plt.plot(x1, y1, color='red', label='width-1.0', linestyle='-', marker='o', linewidth=1.0)

# To display the legend on the plot
plt.legend()

plt.show()
