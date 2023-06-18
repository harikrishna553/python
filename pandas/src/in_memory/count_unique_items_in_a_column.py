import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', None, None, 'Joel', "Joel", "Krishna"],
        'Age': [34, 35, 29, 34, 29, 34, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Hyderabad', 'Bangalore', 'Hyderabad']}

df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

unique_names = df['Name'].unique()
total_unique_names = len(unique_names)

print('\nUnique names : ')
print(unique_names)
print('\nTotal unique names including missing values : ', total_unique_names)

total_unique_names = df['Name'].nunique()
print('\nTotal unique names excluding missing values : ', total_unique_names)

total_unique_names = df['Name'].nunique(dropna=False)
print('\nTotal unique names including missing values : ', total_unique_names)