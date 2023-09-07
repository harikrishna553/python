import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('Salary_Data.csv')

label_encoder = LabelEncoder()

# Create a DataFrame
df = pd.DataFrame(data)

df['City'] = label_encoder.fit_transform(df['City'])
df['Designation'] = label_encoder.fit_transform(df['Designation'])

# Let's assume you have a target variable (e.g., 'a') and want to select features to predict it.
target_variable = 'Salary'

# Create a DataFrame of features (excluding the target variable)
X = df.drop(target_variable, axis=1)

# Create a Series for the target variable
y = df[target_variable]

# Perform feature selection using correlation
# For simplicity, let's select features that have a correlation coefficient greater than 0.3 with the target variable.
correlation_threshold = 0.2
correlations = X.corrwith(y)
print(correlations)
selected_features = X.columns[correlations.abs() > correlation_threshold]

# You can also perform feature selection using other techniques like statistical tests or domain knowledge.

# Print the selected features
print("\nSelected Features:")
print(selected_features)
