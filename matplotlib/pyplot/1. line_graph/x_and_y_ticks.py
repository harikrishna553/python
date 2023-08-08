import matplotlib.pyplot as plt

# Sample data
year = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
population = [1246.2, 1262.6, 1279.7, 1297.4, 1315.8, 1334.9, 1354.7, 1374.2, 1407.6, 1417.2]

# Create a line plot
plt.plot(year, population)

# Custom x-axis and y-axis ticks and labels
custom_xticks = [2010, 2012, 2014, 2016, 2018, 2020, 2022]  # Custom x-axis tick positions
custom_yticks = [1100, 1150, 1200, 1250, 1300, 1400, 1500]  # Custom y-axis tick positions
# custom_xtick_labels = [2010, 2012, 2014, 2016, 2018, 2020, 2022]  # Custom x-axis tick labels
custom_ytick_labels = ['11k', '11.5k', '12k', '12.5k', '13k', '14k', '15k']  # Custom y-axis tick labels

# Apply custom ticks and labels
plt.xticks(custom_xticks)
plt.yticks(custom_yticks, custom_ytick_labels)

# Add gridlines for better readability
plt.grid()

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Population in Millions')
plt.title('India Population in millions by year wise', verticalalignment='center',
          horizontalalignment='center',  color='blue', fontweight='bold',
          backgroundcolor='lightblue')

# Display the plot
plt.show()

