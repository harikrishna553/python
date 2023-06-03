import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Percentage': [np.nan, 76, np.nan, 100, 87, 89]}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

print('\nAssign ranks based on student percentages')
df['Rank'] = df['Percentage'].rank(ascending=False)
df = df.sort_values('Rank')
print(df)

print('\nAssign ranks based on student percentages and na_option="top"')
df['Rank'] = df['Percentage'].rank(ascending=False, na_option='top')
df = df.sort_values('Rank')
print(df)

print('\nAssign ranks based on student percentages and na_option="bottom"')
df['Rank'] = df['Percentage'].rank(ascending=False, na_option='bottom')
df = df.sort_values('Rank')
print(df)