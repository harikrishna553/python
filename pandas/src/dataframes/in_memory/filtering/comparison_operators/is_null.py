import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', None, 'Hyderabad', 'Chennai', 'Bangalore', None],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Percentage': [np.nan, 76, 67, 100, np.nan, 89]}

df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

print('\nGet all the persons whose City do not have any information')
city_info_missed = df['City'].isnull()
city_info_missed_rows = df[city_info_missed]
print(city_info_missed_rows)

print('\nGet all the persons whose Percentage do not have any information')
percentage_info_missed = df['Percentage'].isnull()
percentage_info_missed_rows = df[percentage_info_missed]
print(percentage_info_missed_rows)