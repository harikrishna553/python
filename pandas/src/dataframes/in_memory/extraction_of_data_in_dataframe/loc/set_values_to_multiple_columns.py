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

# Setting the value of a specific row and column
row_label = 'Krishna'
column_to_update = 'City'
df.loc[row_label, column_to_update] = 'Chennai'
print('\nSetting te City of Krishna to "Chennai"')
print(df)

# Setting the value of a specific row and multiple columns
row_label = 'Krishna'
columns_to_update = ['Age', 'Rating']
df.loc[row_label, columns_to_update] = [45, 35]
print('\nUpdating the Age and Rating of Krishna')
print(df)