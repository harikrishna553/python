import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Percentage': [98, 76, 99, 100, 87, 100]}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

print('\nAssign ranks based on student percentages')
df['Rank'] = df['Percentage'].rank(ascending=False)
df = df.sort_values('Rank')
print(df)

print('\nAssign ranks based on student percentages and method="min"')
df['Rank'] = df['Percentage'].rank(ascending=False, method='min')
df = df.sort_values('Rank')
print(df)

print('\nAssign ranks based on student percentages and method="max"')
df['Rank'] = df['Percentage'].rank(ascending=False, method='max')
df = df.sort_values('Rank')
print(df)

print('\nAssign ranks based on student percentages and method="first"')
df['Rank'] = df['Percentage'].rank(ascending=False, method='first')
df = df.sort_values('Rank')
print(df)

print('\nAssign ranks based on student percentages and method="dense"')
df['Rank'] = df['Percentage'].rank(ascending=False, method='dense')
df = df.sort_values('Rank')
print(df)

print('\nAssign ranks based on student percentages and method="dense and convert the ranks to integers"')
df['Rank'] = df['Percentage'].rank(ascending=False, method='dense').astype('int')
df = df.sort_values('Rank')
print(df)




