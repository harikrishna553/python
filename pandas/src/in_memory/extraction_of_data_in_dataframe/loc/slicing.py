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

row_label_1 = 'Krishna'
row_label_2 = 'Chamu'

column_label_1 = 'Age'
column_label_2 = 'Gender'

# Slicing rows based on index labels
result = df.loc[row_label_1:row_label_2]
print('\nSlicing rows based on index labels:\n',result)

# Slicing rows and selecting specific columns
result = df.loc[row_label_1:row_label_2, column_label_1:column_label_2]
print('\nSlicing rows and selecting specific columns\n',result)