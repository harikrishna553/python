import matplotlib.pyplot as plt

data1 = list(range(1, 100))
data2 = list(range(1, 75, 3))
data3 = list(range(1, 50, 4))
data4 = list(range(1, 30, 5))
data5 = list(range(1, 25, 6))

labels = ['Box1', 'Box2', 'Box3', 'Box4', 'Box5']
colors = ['r', 'green', '#fedcba', (0, 1, 1), (1, 0, 0, 0.5)]
data = [data1, data2, data3, data4, data5]

# Create the box plot
boxes = plt.boxplot(data, labels=labels,  patch_artist=True)
index = 0
for box in boxes['boxes']:
    box.set(color='b', linewidth=2, facecolor=colors[index])
    index = index + 1

# Show the plot
plt.show()
