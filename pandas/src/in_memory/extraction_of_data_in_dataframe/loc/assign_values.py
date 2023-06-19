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

row_label = 'Joel'
column_label = 'City'
new_value = 'Delhi'
# Assign a value to a specific cell
df.loc[row_label, column_label] = new_value
print('\nSetting Joel\' City to Delhi.\n', df)

# Assign a value to multiple cells based on a condition
df.loc[df['City'] == 'Hyderabad', 'City'] = 'Mumbai'
print('\nSetting the city to Mumbai where the City is Hyderabad.\n',df)
