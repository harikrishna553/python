import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Krishna', "Raj"],
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

row_label_1 = 'Krishna'
row_label_2 = 'Chamu'

column_label_1 = 'City'
column_label_2 = 'Age'

# Access a single row by its label
result = df.loc[row_label_1]
print('\nAccess a single row by its label :\n',result)

# Access multiple rows by their labels
result = df.loc[[row_label_1, row_label_2]]
print('\nAccess multiple rows by their labels :\n',result)

# Access specific column of the row
result = df.loc[row_label_1, column_label_1]
print('\nAccess specific column of the row :\n',result)

# Access specific columns of the row
result = df.loc[row_label_1, [column_label_1, column_label_2]]
print('\nAccess specific columns of the row :\n',result)

# Access multiple rows and columns
result = df.loc[[row_label_1, row_label_2], [column_label_1, column_label_2]]
print('\nAccess multiple rows and columns :\n',result)

# Access all rows for specific columns
result = df.loc[:, [column_label_1, column_label_2]]
print('\nAccess all rows for specific columns :\n',result)