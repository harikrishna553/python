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
print(df)

print('\nDrop row with any missing values')
drop_row_with_any_missing_values = df.dropna()
print(drop_row_with_any_missing_values)

print('\nDrop row with any missing values')
drop_row_with_any_missing_values = df.dropna(how = 'any')
print(drop_row_with_any_missing_values)

print('\nDrop row with all missing values')
drop_row_with_all_missing_values = df.dropna(how = 'all')
print(drop_row_with_all_missing_values)

print('\nDrop rows with the value for "D" is missing')
drop_row_with_missing_d_value = df.dropna(subset = ['D'])
print(drop_row_with_missing_d_value)

print('\nDrop rows with the value for "C" or "D" is missing')
drop_row_with_missing_c_or_d_value = df.dropna(subset = ['C', 'D'])
print(drop_row_with_missing_c_or_d_value)

print('\nDrop rows with the value for "C" and "D" is missing')
drop_row_with_missing_c_and_d_value = df.dropna(subset = ['C', 'D'], how='all')
print(drop_row_with_missing_c_and_d_value)