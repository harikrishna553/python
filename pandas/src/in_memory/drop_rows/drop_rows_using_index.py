import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Rating': [81, 76, 67, 100, 87, 89]}

df = pd.DataFrame(data)
df_without_row_2 = df.drop(2)
df_drop_rows_3_and_5 = df.drop([3, 5])

print('Original DataFrame')
print(df)

print('\ndf_without_row_2')
print(df_without_row_2)

print('\ndf_drop_rows_3_and_5')
print(df_drop_rows_3_and_5)

df.drop([3, 5], inplace=True)
print('\nOriginal DataFrame after dropping rows 3 and 5')
print(df)