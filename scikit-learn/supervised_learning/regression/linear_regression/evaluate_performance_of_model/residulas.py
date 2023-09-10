import numpy as np
import matplotlib.pyplot as plt

# Generate some data
year = np.array([2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015])
actual_population = np.array([1425.776, 1417.173, 1407.564, 1396.387, 1384.332, 1371.818, 1359.003, 1346.021, 1332.993])

# Fit two different regression models to the data
model1 = np.polyfit(year, actual_population, 1)

# Predict the values for both models
m = model1[0]
c = model1[1]
predicted_population = m * year + c

# Calculate residuals
residuals = actual_population - predicted_population

print("Actual Values:", actual_population)
print("Predicted Values:", predicted_population)
print("Residuals:", residuals)

# Create a scatterplot of residuals
plt.scatter(np.arange(len(residuals)), residuals, c='blue', marker='o', label='Residuals')

# Add a horizontal line at y=0 for reference
plt.axhline(y=0, color='red', linestyle='--', linewidth=1, label='Zero Residual Line')

# Add labels and a legend
plt.xlabel('Data Point')
plt.ylabel('Residual')
plt.title('Residual Plot')
plt.legend()

# Show the plot
plt.grid()
plt.show()
