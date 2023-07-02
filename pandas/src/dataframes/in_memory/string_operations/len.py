import pandas as pd

# Create a sample DataFrame
data = {'Name': ['krishna gurram', 'sailu nava', 'joel chelli', 'chamu mag', 'Jitendra khod', "Krishna battu"],
        'Age': [34, 35, 234, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Rating': [67, 43, 67, 100, 41, 89]}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

df['No_of_chars_in_city'] = df['City'].str.len()

print('\nDataFrame after adding new column NoOfCharsInCity\n', df)