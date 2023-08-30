import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load data from CSV file
data = pd.read_csv('system_metrics_data.csv')

# Print the column names
print("Column Names:")
print(data.columns)

print(data)
# Separate features (X) and labels (y)
y = data['application_state']
X = data[['cpu_usage', 'memory_usage', 'disk_usage', 'network_latency']]


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a DecisionTreeClassifier
clf = DecisionTreeClassifier()

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Predict the application states for the test data
y_pred = clf.predict(X_test)

# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Predicted application states:", y_pred)
# print("True application states:", y_test)
print("Accuracy:", accuracy)
