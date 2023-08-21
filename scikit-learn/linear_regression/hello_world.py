import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

x = np.arange(1, 100)
y = 235.456 * x + 123.876
random_values = (100) * np.random.randn(len(y))
y = y + random_values

data = {
    'x': x,
    'y': y
}
df = pd.DataFrame(data)

# Split the data into features (X) and target (y)
X = df[['x']]
y = df[['y']]


# Split the data into training and testing sets
X_train = X[:80]
y_train = y[:80]
X_test = X[80:]
y_test = y[80:]

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
# plt.scatter(X_train, y_train, color='blue', label='Actual')
print(type(X_test))
plt.scatter(X_test, y_test, color='red', label='Actual')
plt.scatter(X_test, y_pred, color='black', label='Predicted')

plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Linear Regression Example')
plt.show()
