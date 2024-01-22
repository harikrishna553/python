import matplotlib.pyplot as plt

# Sample data
no_of_entries = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]
default_map = [84, 792, 1036, 295, 251, 164,  ]

# Create a line plot
plt.plot(no_of_entries, default_map)

# Add grid lines
plt.grid()

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Population in Millions')
plt.title('India Population in millions by year wise', verticalalignment='center',
          horizontalalignment='center',  color='blue', fontweight='bold',
          backgroundcolor='lightblue')

# Display the plot
plt.show()

