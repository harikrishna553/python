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

print('\nRename the columns "Name" to "User_Name" and "City" to "User_City"')
new_column_names = {'Name': 'User_Name', 'City': 'User_City'}
df = df.rename(columns=new_column_names)
print(df)