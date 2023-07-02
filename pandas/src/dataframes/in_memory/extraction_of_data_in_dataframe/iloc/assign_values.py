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

row_index = 1
column_index = 0
# Assign a value to a specific cell
print('\nSet the Name of row index 1 to Harika')
df.iloc[row_index, column_index] = 'Harika'
print(df)

# Assign a value to multiple cells based on a condition
column_index = 2
print('\nSet the city of all the people living in Hyderabad to Mumbai')
df.iloc[df['City'] == 'Hyderabad', column_index] = 'Mumbai'
print(df)