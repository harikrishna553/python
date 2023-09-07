import matplotlib.pyplot as plot
import numpy as np

# Sample data
x = np.arange(1, 100)
y = 10 * x + 123

# Plot the data points
plot.plot(x, y, label='y=10x+123')

mean = np.mean(y)
plot.axhline(y=mean, color='green', label=f'Horizontal Line at y={mean}')
text = f'This is y={mean}'
plot.text(30, mean + 10, text, color='red', fontsize=12, ha='center')

# Set labels and legend
plot.legend()

# Show the plot
plot.show()
