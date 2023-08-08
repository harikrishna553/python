import matplotlib.pyplot as plt

# Sample data
x1 = [5, 10, 15, 20, 25]
y1 = [20, 40, 60, 80, 100]

plt.plot(x1, y1, marker='o', mec='red', mew=2)

# To display the legend on the plot
plt.legend()

plt.show()
