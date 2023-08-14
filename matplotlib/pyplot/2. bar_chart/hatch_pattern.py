import matplotlib.pyplot as plt

fruits = ['Apple', 'Banana', 'Orange', 'Grapes']
liked_by_count = [120, 45, 32, 87]
#colors = [(1, 0, 0), 'yellow', 'orange', '#00ff00']

# bars = plt.bar(fruits, liked_by_count, color=colors)
common_background_color = 'lightgray'
bars = plt.bar(fruits, liked_by_count)
for bar in bars:
    bar.set_facecolor(common_background_color)

bars[0].set_hatch('/')
bars[1].set_hatch('.')
bars[2].set_hatch('*')
bars[3].set_hatch('o')

plt.xlabel('Fruits')
plt.ylabel('Liked by people')

plt.title('Bar Chart Example')
plt.show()
