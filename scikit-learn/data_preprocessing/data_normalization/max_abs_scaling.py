import numpy as np
from sklearn.preprocessing import MaxAbsScaler

# Create the training data
X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create the scaler
scaler = MaxAbsScaler()

# Fit the scaler to the training data
scaler.fit(X_train)

# Transform the training data
X_train_scaled = scaler.transform(X_train)

print(X_train_scaled)