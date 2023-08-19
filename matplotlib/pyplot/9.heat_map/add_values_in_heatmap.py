import matplotlib.pyplot as plt
import pandas as pd

import pandas as pd

# Sample data
data = {
    'Company': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'Month': ['Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb', 'Mar', 'Mar', 'Mar'],
    'Sales': [1000, 1500, 1200, 1100, 1200, 1100, 1900, 1400, 800]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Pivot the data for heatmap
heatmap_data = df.pivot(index='Company', columns='Month', values='Sales')
print(heatmap_data)

# Create a heatmap using imshow
plt.imshow(heatmap_data, cmap='viridis', interpolation='nearest')

# Add color bar for reference
plt.colorbar()

# Add text annotations to display values
for i in range(len(heatmap_data)):
    for j in range(len(heatmap_data.columns)):
        plt.text(j, i, heatmap_data.iloc[i, j], ha='center', va='center', color='black')


# Add labels and title
plt.xticks(range(len(heatmap_data.columns)), heatmap_data.columns)
plt.yticks(range(len(heatmap_data.index)), heatmap_data.index)
plt.xlabel('Month')
plt.ylabel('Company')
plt.title('Sales Heatmap')

# Display the heatmap
plt.show()
