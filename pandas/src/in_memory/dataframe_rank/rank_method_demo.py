import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Percentage': [98, 76, 99, 100, 87, 96]}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

print('\nAssign ranks based on student scores')
df['Rank'] = df['Percentage'].rank(ascending=False)
df = df.sort_values('Rank')

print(df)
