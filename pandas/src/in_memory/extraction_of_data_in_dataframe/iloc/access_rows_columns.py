import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Rating': [81, 76, 67, 100, 87, 89]}

df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

row_index_1 = 2
row_index_2 = 4

column_index_1 = 0
column_index_2 = 2

# Access a single row by its integer index
result = df.iloc[row_index_1]
print('\nAccess a single row by its integer index :\n', result)

# Access multiple rows by their integer indices
result = df.iloc[[row_index_1, row_index_2]]
print('\nAccess multiple rows by their integer indices :\n', result)

# Access specific column of the row
result = df.iloc[row_index_1, column_index_1]
print('\nAccess specific column of the row :\n', result)

# Access specific columns of the row
result = df.iloc[row_index_1, [column_index_1, column_index_2]]
print('\nAccess specific columns of the row :\n', result)

# Access multiple rows and columns
result = df.iloc[[row_index_1, row_index_2], [column_index_1, column_index_2]]
print('\nAccess multiple rows and columns :\n', result)
