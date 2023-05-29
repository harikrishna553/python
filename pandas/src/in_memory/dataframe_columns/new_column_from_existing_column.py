import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Ram', 'Joel', 'Gopi', 'Jitendra', "Raj"],
        'Age': [34, 25, 29, 41, 52, 23],
        'City': ['Bangalore', 'Chennai', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Chennai']}

df = pd.DataFrame(data)
print(df)

print('\nAdd new columns Age_plus_10, Age_minus_10')
df['Age_plus_10'] = df['Age'] + 10
print(df)

df['Age_minus_10'] = df['Age'].sub(10)
print(df)

df['City_in_upper_case'] = df['City'].str.upper()
print(df)