import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Krishna', 'Joel', "Krishna", "Krishna"],
        'Age': [34, 35, 29, 34, 29, 34, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Hyderabad', 'Bangalore', 'Hyderabad']}

df = pd.DataFrame(data)
df_unique = df.drop_duplicates()

print('Original DataFrame')
print(df)

print('\nData after dropping duplicates')
print(df_unique)

df_unique_by_name_and_age = df.drop_duplicates(subset=['Name', 'Age'])
print('\nData set unique by Name and Age')
print(df_unique_by_name_and_age)

df_unique_by_name_and_age_keep_last = df.drop_duplicates(subset=['Name', 'Age'], keep='last')
print('\nData set unique by Name and Age and keep last values')
print(df_unique_by_name_and_age_keep_last)

df_unique_by_name_and_age_keep_none= df.drop_duplicates(subset=['Name', 'Age'], keep=False)
print('\nData set unique by Name and Age and do not keep duplicate rows')
print(df_unique_by_name_and_age_keep_none)