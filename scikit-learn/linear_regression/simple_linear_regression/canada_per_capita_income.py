import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

import os

csv_file = os.getcwd() + '/data/csvs/Canada_per_capita_income.csv'

# Read the CSV file
df = pd.read_csv(csv_file)

# Split the data into features (X) and target (y)
X = df[['year']]
y = df[['income']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the linear regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)

# Print the coefficients and MSE
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mse)

# Plot the data and regression line
# plt.plot(df["year"], df["income"], marker='o')
plt.scatter(X_train, y_train, color='blue', label='Trained Data')
plt.scatter(X_test, y_test, color='red', label='Actual')
plt.scatter(X_test, y_pred, color='black', label='Predicted')

plt.legend()
plt.xlabel('Year')
plt.ylabel('Income')
plt.title('Linear Regression Example')
plt.show()

# Years for prediction
years_to_predict = [2020, 2021, 2022, 2023]

# Create a DataFrame for the years to predict
future_years = pd.DataFrame({'year': years_to_predict})

# Predict the per capita income for the future years
predicted_per_capita_income = model.predict(future_years)

# Add the predictions to the DataFrame
future_years['income'] = predicted_per_capita_income

print(future_years)