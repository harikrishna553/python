import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu'],
        'Age': [34, 35, 29, 35],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female'],
        'Rating': [81, 76, 67, 100]}

df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

print('\nSet "Name" column as index column')
df.set_index('Name', inplace=True)
print(df)

print('\nRenaming the user names')
new_names = {'Krishna': 'Ram', 'Sailu': 'Harika'}
df.rename(new_names, axis=0, inplace=True )
print(df)