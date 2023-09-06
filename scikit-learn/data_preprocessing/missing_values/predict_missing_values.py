from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'a' : [1, 2, 3, 4, 5, 6, 7],
    'b' : [12.3, np.NAN, 143.45, np.NAN, 34, 56, 109],
    'c' : [7, 6, 5, 4, 3, 2, 1]
})

print(f'df : \n', df)

# Separate data into two sets: rows with missing values and rows without missing values
rows_with_missing_values = df[df['b'].isnull()]
rows_without_missing_values = df.dropna(subset=['b'])

# Train a model to predict the missing values
model = LinearRegression()
model.fit(rows_without_missing_values.drop('b', axis=1), rows_without_missing_values['b'])

# Predict missing values
predicted_values = model.predict(rows_with_missing_values.drop('b', axis=1))
rows_with_missing_values['b'] = predicted_values

# Concatenate the data back together and reset the index
df = pd.concat([rows_with_missing_values, rows_without_missing_values], ignore_index=True)
print(f'df after imputation: \n', df)
