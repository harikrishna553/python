import numpy as np
import matplotlib.pyplot as plt

# Mean absolute error
def mae(actual, predicted):
    # Calculate absolute residuals
    absolute_residuals = np.abs(actual - predicted)

    # Calculate mean absolute error (MAE)
    mae = np.mean(absolute_residuals)

    return mae

# Generate some data
year = np.array([2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015])
population_in_millions = np.array([1425.776, 1417.173, 1407.564, 1396.387, 1384.332, 1371.818, 1359.003, 1346.021, 1332.993])

# Fit two different regression models to the data
model1 = np.polyfit(year, population_in_millions, 1)
model2 = np.polyfit(year, population_in_millions, 2)

# Predict the values for both models
m1 = model1[0]
c1 = model1[1]
population_pred1 =  m1 * year + c1

a1 = model2[0]
a2 = model2[1]
a3 = model2[2]
population_pred2 = a1 * year**2 + a2 * year + a3

# print(f'population_pred1 : {population_pred1}')
# print(f'population_pred2 : {population_pred2}')

# Calculate the MSE for both models
mae1 = mae(population_in_millions, population_pred1)
mae2 = mae(population_in_millions, population_pred2)

print("MAE for model1:", mae1)
print("MAE for model2:", mae2)

if mae1 > mae2:
    print('prediction2 is more accurate')
else:
    print('prediction1 is more accurate')

# Draw the plot
plt.plot(year, population_in_millions, color='red')
plt.plot(year, population_pred1, color='blue', label=f'pred1 : {m1}*x+{c1}')
plt.plot(year, population_pred2, color='green', label=f'pred2 : {a1}*x*x+{a2}*x+{a3}')

plt.legend()

plt.show()



