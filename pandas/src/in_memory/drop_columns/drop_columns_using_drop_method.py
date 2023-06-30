import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Rating': [81, 76, 67, 100, 87, 89]}

df = pd.DataFrame(data)
df_drop_column_age = df.drop(columns='Age')
df_drop_column_age_and_city = df.drop(columns=['Age', 'City'])

print('Original DataFrame')
print(df)

print('\ndf_drop_column_age')
print(df_drop_column_age)

print('\ndf_drop_column_age_and_city')
print(df_drop_column_age_and_city)

df.drop(columns=['Age', 'City'], inplace=True)
print('\nOriginal DataFrame')
print(df)