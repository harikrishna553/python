import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'A' : [1, 2, np.nan, 3, 4, np.nan, 5],
    'B' : [1, np.nan, np.nan, 3, 4, 5, 6],
    'C' : [1, 2, np.nan, 4, 5, np.nan, 6],
    'D' : ['a', 'b', None, None, 'c', 'd', 'e']
}

df = pd.DataFrame(data)
df_without_missing_values = df.fillna(0)

print('Original DataFrame')
print(df)

print('\nDataFrame by filling with 0')
print(df_without_missing_values)

df.fillna(0, inplace=True)
print('\nOriginal DataFrame by filling with the argument inplace=True')
print(df)