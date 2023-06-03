import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, np.nan, 52, np.nan],
        'City': ['Bangalore', 'Hyderabad', None, 'Chennai', None, 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male']}
df = pd.DataFrame(data)

sort_by_age_ascending_1 = df.sort_values('Age')
sort_by_age_ascending_2 = df.sort_values('Age', na_position='last')

sort_by_age_ascending_none_to_first_1 = df.sort_values('Age', na_position='first')

print('df : \n', df)
print('\nsort_by_age_ascending_1 : \n', sort_by_age_ascending_1)
print('\nsort_by_age_ascending_2 : \n', sort_by_age_ascending_2)
print('\nsort_by_age_ascending_none_to_first_1 : \n', sort_by_age_ascending_none_to_first_1)