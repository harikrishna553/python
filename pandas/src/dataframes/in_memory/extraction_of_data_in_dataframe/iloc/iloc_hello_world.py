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

row_at_1st_position = df.iloc[0]
row_at_2nd_position = df.iloc[1]
print('\nrow_at_1st_position : \n', row_at_1st_position)
print('\nrow_at_2nd_position : \n', row_at_2nd_position)

rows_at_2nd_4th_positions = df.iloc[[2, 4]]
print('\nrows_at_2nd_4th_positions: \n', rows_at_2nd_4th_positions)

try:
    print('\nTrying to access the element at index 10')
    print(df.iloc[10])
except IndexError as e:
    print(e)
