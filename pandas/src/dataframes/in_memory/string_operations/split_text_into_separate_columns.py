import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna,Gurram', 'Sailu,Dokku', 'Joel,Chelli', 'Chamu,Maj', 'Gopi,Battu', "Siva,Ponnam"],
        'Age': [34, 35, 234, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Hobbies': ['Football,Cricket,Tennis', 'Tennis, cricket,Trekking', 'Trekking, reading books', 'Chess', 'Read Books', 'Cricket']}

df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

name_split_df = df['Name'].str.split(',', expand=True)
print('\nname_split_df\n',name_split_df)

# Assign the splits to FirstName and LastName columns
df[['FirstName', 'LastName']] = name_split_df

# You can use below statements also to achieve the same result
# df['FirstName'] = name_split_df[0]
# df['LastName'] = name_split_df[1]


print('\nDataFrame after adding FirstName and LastName columns')
print(df)