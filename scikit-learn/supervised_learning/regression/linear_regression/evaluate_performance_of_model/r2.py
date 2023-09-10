import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Generate some data
year = np.array([2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015])
population_in_millions = np.array([1425.776, 1417.173, 1407.564, 1396.387, 1384.332, 1371.818, 1359.003, 1346.021, 1332.993])

# Fit two different regression models to the data
model1 = np.polyfit(year, population_in_millions, 1)
model2 = np.polyfit(year, population_in_millions, 2)

# Calculate predicted values for both models
predicted1 = np.polyval(model1, year)
predicted2 = np.polyval(model2, year)

# Calculate R-squared for both models
r2_model1 = r2_score(population_in_millions, predicted1)
r2_model2 = r2_score(population_in_millions, predicted2)

print("R2 for model1:", r2_model1)
print("R2 for model2:", r2_model2)

if r2_model1 > r2_model2:
    print('prediction1 is more accurate')
else:
    print('prediction2 is more accurate')

# Draw the plot
plt.plot(year, population_in_millions, color='red')
plt.plot(year, predicted1, color='blue', label=f'predicted1')
plt.plot(year, predicted2, color='green', label=f'predicted2')

plt.legend()

plt.show()



