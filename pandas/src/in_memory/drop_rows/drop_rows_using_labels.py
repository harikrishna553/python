import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Rating': [81, 76, 67, 100, 87, 89]}

df = pd.DataFrame(data)
df.set_index('Name', inplace=True)

df_drop_krishna = df.drop('Krishna')
df_drop_krishna_and_chamu = df.drop(['Krishna', 'Chamu'])

print('Original DataFrame')
print(df)

print('\nRow with label "Krishna" is deleted')
print(df_drop_krishna)

print('\nRow with label "Krishna" and "Chamu" are deleted')
print(df_drop_krishna_and_chamu)

df.drop(['Krishna', 'Chamu'], inplace=True)
print('\nOriginal DataFrame after dropping rows with labels "Krishna" and "Chamu"')
print(df)