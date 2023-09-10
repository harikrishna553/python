import pandas as pd
from sklearn.preprocessing import StandardScaler

# Create a sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9],
    'D' : [True, False, False]
}

df = pd.DataFrame(data)

# Create a StandardScaler instance
scaler = StandardScaler()

# Select numeric columns
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Transform the selected columns
standardized_values = scaler.fit_transform(df[numeric_columns])

print(f'type of standardized_values : {type(standardized_values)}')
print(f'standardized_values : \n{standardized_values}')
