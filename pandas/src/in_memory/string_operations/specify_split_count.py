import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna,Gurram', 'Sailu,Dokku', 'Joel,Chelli', 'Chamu,Maj', 'Gopi,Battu', "Siva,Ponnam"],
        'Age': [34, 35, 234, 35, 52, 34],
        'Hobbies': ['Football,Cricket,Tennis', 'Tennis, cricket,Trekking', 'Trekking, reading books', 'Chess', 'Read Books', 'Cricket']}

df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

hobbies_split_df = df['Hobbies'].str.split(',', expand=True, n=1)
print('\nhobbies_split_df\n',hobbies_split_df)

# Assign the splits to FirstName and LastName columns
df[['FirstHobby', 'RestOfHobbies']] = hobbies_split_df

print('\nDataFrame after adding FirstHobby and RestOfHobbies columns')
print(df)