import numpy as np
import matplotlib.pyplot as plt

# Sample data
house_prices = np.array([100000, 120000, 150000, 170000, 200000, 700000, 200])

# Calculate Q1, Q3, and IQR
Q1 = np.percentile(house_prices, 25)
Q3 = np.percentile(house_prices, 75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Create a box plot
plt.figure(figsize=(8, 6))
plt.boxplot(house_prices, vert=False)

# Highlight outliers with red color
outlier_color = dict(markerfacecolor='r', marker='o', markersize=8, linestyle='none')
plt.boxplot(house_prices, vert=False, flierprops=outlier_color)

# Annotate the plot with Q1, Q3, and IQR values
# plt.text(Q1, 1.05, f'Q1 = {Q1}', fontsize=12, color='b', horizontalalignment='center')
# plt.text(Q3, 1.05, f'Q3 = {Q3}', fontsize=12, color='b', horizontalalignment='center')
# plt.text((Q1 + Q3) / 2, 1.15, f'IQR = {IQR}', fontsize=12, color='b', horizontalalignment='center')
# plt.text(lower_bound, 1.25, f'Lower IQR Bound = {lower_bound}', fontsize=12, color='g', horizontalalignment='center')
# plt.text(upper_bound, 1.25, f'Upper IQR Bound = {upper_bound}', fontsize=12, color='g', horizontalalignment='center')

# Create a custom legend label
custom_legend_label = [
    plt.Line2D([0], [0], marker='o', color='r', label='Outliers', markersize=8, linestyle='none'),
    plt.Line2D([0], [0], marker='', color='b', label=f'Q1 = {Q1}', markersize=0, linestyle='-'),
    plt.Line2D([0], [0], marker='', color='b', label=f'Q3 = {Q3}', markersize=0, linestyle='-'),
    plt.Line2D([0], [0], marker='', color='b', label=f'IQR = {IQR}', markersize=0, linestyle='-'),
    plt.Line2D([0], [0], marker='', color='g', label=f'Lower IQR Bound = {lower_bound}', markersize=0, linestyle='-'),
    plt.Line2D([0], [0], marker='', color='g', label=f'Upper IQR Bound = {upper_bound}', markersize=0, linestyle='-')
]

# Add the custom legend label to the plot
plt.legend(handles=custom_legend_label, loc='upper right')

plt.xlabel('House Price (in USD)')
plt.title('House Prices with Quartiles and IQR Values')
plt.grid(True)

plt.show()
