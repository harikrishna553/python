import matplotlib.pyplot as plt

# Sample data
year = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
population = [1246.2, 1262.6, 1279.7, 1297.4, 1315.8, 1334.9, 1354.7, 1374.2, 1407.6, 1417.2]

# Create a line plot
plt.plot(year, population)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Population in Millions')
plt.title('India Population in millions by year wise', verticalalignment='center',
          horizontalalignment='center',  color='blue', fontweight='bold',
          backgroundcolor='lightblue')

# Display the plot
plt.show()

