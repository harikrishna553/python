import matplotlib.pyplot as plot
import numpy as np

# Sample data
x = np.arange(1, 100)
y = 10 * x + 123

# Plot the data points
plot.plot(x, y, label='y=10x+123')

median = np.median(x)

plot.axvline(x=median, color='red', label=f'Vertical Line at x={median}')
text = f'This is x={median}'
plot.text(median+15, 1000, text, color='red', fontsize=12, ha='center')

# Set labels and legend
plot.legend()

# Show the plot
plot.show()
