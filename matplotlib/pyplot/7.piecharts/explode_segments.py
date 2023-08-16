import matplotlib.pyplot as plt

plt.title('Favourite Sports percentage')

# Sample data and labels
categories = ['Football', 'Basketball', 'Chess', 'Cricket', 'Others']
values = [25, 35, 10, 20, 10]
explode = [0, 0, 0, 0, 0.3]

# Create a pie chart
plt.pie(values, labels=categories, autopct='%1.1f%%', explode=explode)

plt.show()