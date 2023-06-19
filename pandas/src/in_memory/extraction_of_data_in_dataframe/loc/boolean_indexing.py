import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Ram', "Raj"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Rating': [81, 76, 67, 100, 87, 89]}

df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

print('\nSet "Name" column as index column')
df.set_index('Name', inplace=True)
print(df)

# Access rows based on a condition
age_greater_34 = df.loc[df['Age'] > 34]
print('\nage_greater_34\n',age_greater_34)

# Access rows based on multiple conditions
age_greater_34_city_hyderabad = df.loc[(df['Age'] > 34) & (df['City'] == 'Hyderabad')]
print('\nage_greater_34_city_hyderabad:\n',age_greater_34_city_hyderabad)