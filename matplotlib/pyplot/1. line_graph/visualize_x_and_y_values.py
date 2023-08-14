import matplotlib.pyplot as plt

# Sample data
x_data = [1, 2, 3, 4, 5, 6]
y_data = [10, 43, 23, 6, 90, 65]

# Create a scatter plot with marker points
plt.scatter(x_data, y_data, color='blue', marker='x', label='Data Points display demo')

# Annotate marker points with data values
for i, (x, y) in enumerate(zip(x_data, y_data)):
    plt.annotate(f'({x}, {y})', (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='darkred')

# Set labels for the X and Y axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.legend()
plt.title('Scatter Plot with Data Values')
plt.grid(True)
plt.show()
