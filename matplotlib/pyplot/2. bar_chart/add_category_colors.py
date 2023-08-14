import matplotlib.pyplot as plt

fruits = ['Apple', 'Banana', 'Orange', 'Grapes']
liked_by_count = [120, 45, 32, 87]
colors = [(1, 0, 0), 'yellow', 'orange', '#00ff00']

plt.bar(fruits, liked_by_count, color=colors)

plt.xlabel('Fruits')
plt.ylabel('Liked by people')

plt.title('Bar Chart Example')
plt.show()
