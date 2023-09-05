import numpy as np
import matplotlib.pyplot as plt

# Define the sigmoid function
def sigmoid(y):
    return 1 / (1 + np.exp(-y))

# Create a range of values for 'y'
y = np.linspace(-6, 6, 300)

# Calculate sigmoid values for the range of 'z'
sigmoid_values = sigmoid(y)

# Create a plot
plt.figure(figsize=(8, 5))
plt.plot(y, sigmoid_values, label='Sigmoid Function', color='green')
plt.xlabel('y')
plt.ylabel('sigmoid(y)')
plt.title('Sigmoid Function')

plt.axhline(y=1, color='black', linestyle='--', linewidth=0.9)
plt.axhline(y=0.4, color='red', linestyle='--', linewidth=1.5, label='Threshold = 0.4')
plt.axvline(x=0, color='black', linestyle='--', linewidth=0.9)

plt.grid(True, linestyle='--', alpha=0.6)

plt.legend()
plt.show()
