import matplotlib.pyplot as plt
import numpy as np

data = np.random.random((5, 5))

custom_colormap = plt.cm.get_cmap('coolwarm')
plt.imshow(data, cmap=custom_colormap, vmin=0.2, vmax=0.8)

plt.colorbar()
plt.title('Modified Colormap Range')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
