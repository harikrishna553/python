import matplotlib.pyplot as plt
import numpy as np

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(nrows=2, ncols=2)
fig.suptitle('Sub plots demo', fontsize=16)

x1 = np.array([2, 3, 5, 7, 11, 13, 17])
y1 = 5 * x1 + 345

x2 = np.array([17, 13, 11, 7, 5, 3, 2])
y2 = 5 * x2 + 345

categories = ['Apple', 'Banana', 'Orange', 'Grapes']
liked_by_count = [120, 45, 32, 87]

# Plot data in each subplot
axs[0, 0].plot(x1, y1)
axs[0, 1].scatter(x2, y2)

axs[1, 0].bar(categories, liked_by_count)
colors = ['r', 'green', '#fedcba', (0, 1, 1), (1, 0, 0, 0.5)]

axs[1, 1].pie(liked_by_count, labels=categories, autopct='%1.1f%%', colors=colors)

# Customize each subplot as needed
axs[0, 0].set_title('Line Plot')
axs[0, 0].set_xlabel('primes')
axs[0, 0].set_ylabel('y=5x+345')

# Customize each subplot as needed
axs[0, 1].set_title('Scatter Plot')
axs[0, 1].set_xlabel('primes')
axs[0, 1].set_ylabel('y=5x+345')

# Add titles, labels, legends, etc., to other subplots similarly

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the figure
plt.show()
