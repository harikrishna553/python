import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, np.nan, 52, np.nan],
        'City': ['Bangalore', 'Hyderabad', None, 'Chennai', None, 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male']}
df = pd.DataFrame(data)

sort_by_name_ascending_1 = df.sort_values('Name')
sort_by_name_ascending_2 = df.sort_values(by='Name')
sort_by_name_ascending_3 = df.sort_values(by='Name', ascending=True)
sort_by_name_ascending_4 = df.sort_values('Name', ascending=True)

print('df : \n', df)
print('\nsort_by_name_ascending_1 : \n', sort_by_name_ascending_1)
print('\nsort_by_name_ascending_2 : \n', sort_by_name_ascending_2)
print('\nsort_by_name_ascending_3 : \n', sort_by_name_ascending_3)
print('\nsort_by_name_ascending_4 : \n', sort_by_name_ascending_4)

print('\nSort by Name in descending order\n')
sort_by_name_descending_1 = df.sort_values('Name', ascending=False)
print('\nsort_by_name_descending_1 : \n', sort_by_name_descending_1)
