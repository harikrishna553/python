import numpy as np
from sklearn.ensemble import IsolationForest

# Data points
data = np.array([100000, 120000, 150000, 170000, 200000, 700000, 200]).reshape(-1, 1)

# Create an Isolation Forest model
model = IsolationForest(contamination='auto', random_state=42)

# Fit the model to the data
model.fit(data)

# Predict outliers/anomalies
outliers = model.predict(data)

# Find and print the outlier numbers
outlier_indices = np.where(outliers == -1)[0]
outlier_values = data[outlier_indices]

print("Outlier Numbers:", outlier_values)
