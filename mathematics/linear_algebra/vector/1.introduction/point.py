import numpy as np
import matplotlib.pyplot as plt

x = [2]
y = [3]

plt.scatter(x, y, label='point=[2, 3]')

plt.title('Point in two dimensional space')

plt.legend()
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([1, 2, 3, 4, 5])
plt.show()