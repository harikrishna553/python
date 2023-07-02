import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Ram', 'Ravi', 'Joel', "Joel"],
        'Age': [34, 35, 29, 34, 29, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Hyderabad', 'Bangalore']}

df = pd.DataFrame(data)
print('\nSet the Name column as index')

new_df = df.set_index(keys=['Name'])

print('Original DataFrame')
print(df)

print('\nDataFrame where Name is the index')
print(new_df)

df.set_index(keys=['Name'], inplace=True)
print('\nOriginal DataFrame')
print(df)

df.reset_index(inplace=True)
print('\nOriginal DataFrame after resetting the index')
print(df)
