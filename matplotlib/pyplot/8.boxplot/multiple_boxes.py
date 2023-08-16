import matplotlib.pyplot as plt

data1 = list(range(1, 100))
data2 = list(range(1, 75, 3))
data3 = list(range(1, 50, 4))

labels = ['Box1', 'Box2', 'Box3']

# Create the box plot
plt.boxplot([data1, data2, data3], labels=labels)

# Show the plot
plt.show()
