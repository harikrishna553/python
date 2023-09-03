import numpy as np
import matplotlib.pyplot as plt

# Generate some random data with a mean of 0 and standard deviation of 1
house_prices = [50000, 300000, 950000, 500000, 750000, 100000, 325000, 650000, 25000, 200000, 35000]

# Calculate quartiles
q1 = np.percentile(house_prices, 25)  # Q1 (First Quartile)
q3 = np.percentile(house_prices, 75)  # Q3 (Third Quartile)

# Create the box plot
plt.boxplot(house_prices)

# Label the quartiles
plt.text(0.85, q1, f'Q1: {q1}', va='center', ha='left', bbox=dict(facecolor='white', edgecolor='black'))
plt.text(0.85, q3, f'Q3: {q3}', va='center', ha='left', bbox=dict(facecolor='white', edgecolor='black'))

# Set labels and title
plt.ylabel('Exam Scores')
plt.title('Box Plot with Q1 and Q3 Quartiles')

# Show the plot
plt.show()