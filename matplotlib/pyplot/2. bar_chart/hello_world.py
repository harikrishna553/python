import matplotlib.pyplot as plt

fruits = ['Apple', 'Banana', 'Orange', 'Grapes']
liked_by_count = [120, 45, 32, 87]

plt.bar(fruits, liked_by_count)
plt.xlabel('Fruits')
plt.ylabel('Liked by people')

plt.title('Bar Chart Example')
plt.show()
