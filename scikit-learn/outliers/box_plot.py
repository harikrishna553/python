import matplotlib.pyplot as plt
import numpy as np

# Create some sample data
house_prices = np.array([100000, 120000, 150000, 170000, 200000, 700000])

# Highlight outliers with red color
outlier_color = dict(markerfacecolor='r', marker='o', markersize=15, linestyle='none')

# Create a box plot of the house prices
plt.boxplot(house_prices, flierprops=outlier_color)
plt.show()