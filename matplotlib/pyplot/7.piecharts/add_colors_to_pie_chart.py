import matplotlib.pyplot as plt

plt.title('Favourite Sports percentage')

# Sample data and labels
categories = ['Football', 'Basketball', 'Chess', 'Cricket', 'Others']
values = [25, 35, 10, 20, 10]
colors = ['r', 'green', '#fedcba', (0, 1, 1), (1, 0, 0, 0.5)]

# Create a pie chart

plt.pie(values, labels=categories, autopct='%1.1f%%', colors=colors)
# plt.legend()
plt.show()