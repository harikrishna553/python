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

row_start_index = 1
row_end_index = 5
step_count = 2
column_start_index = 0
column_end_index = 3
column_index = 0
column_index_1 = 0
column_index_2 = 2

# Slice rows based on integer indices
result = df.iloc[row_start_index:row_end_index]
print('\nSlice rows based on integer indices\n', result)

# Access all the rows from starting to row_end_index
result = df.iloc[:row_end_index]
print('\nAccess all the rows from starting to row_end_index\n', result)

# Access all the rows from row_start_index to end
result = df.iloc[row_start_index:]
print('\nAccess all the rows from row_start_index to end\n', result)

# Slice rows based on integer indices and a step of step_count
result = df.iloc[row_start_index:row_end_index:step_count]
print('\nSlice rows based on integer indices and a step of step_count\n', result)

# Slice rows and select specific columns
result = df.iloc[row_start_index:row_end_index, column_start_index:column_end_index]
print('\nSlice rows and select specific columns\n', result)

# Access all rows for specific column
result = df.iloc[:, column_index]
print('\nAccess all rows for specific column\n', result)

# Access all rows for specific columns
result = df.iloc[:, [column_index_1, column_index_2]]
print('\nAccess all rows for specific columns\n', result)