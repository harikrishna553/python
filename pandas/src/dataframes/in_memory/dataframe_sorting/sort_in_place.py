import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, np.nan, 52, np.nan],
        'City': ['Bangalore', 'Hyderabad', None, 'Chennai', None, 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male']}
df = pd.DataFrame(data)

print('\nSort by Age :')
sort_by_age_ascending = df.sort_values('Age')
print(sort_by_age_ascending)

print('\nOriginal DataFrame')
print(df)

print("Sort by Age in place : ")
df.sort_values('Age', inplace=True)
print('\nOriginal DataFrame')
print(df)