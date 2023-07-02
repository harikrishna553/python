import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna,Gurram', 'Sailu,Dokku', 'Joel,Chelli', 'Chamu,Maj', 'Gopi,Battu', "Siva,Ponnam"],
        'Age': [34, 35, 234, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Hobbies': ['Football,Cricket,Tennis', 'Tennis, cricket,Trekking', 'Trekking, reading books', 'Chess', 'Read Books', 'Cricket']}

df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

name_split_series = df['Name'].str.split(',')
first_names_series = name_split_series.str.get(0)
last_names_series = name_split_series.str.get(1)

df['FirstName'] = first_names_series
df['LastName'] = last_names_series

print('\nname_split_series\n',name_split_series)
print('\nfirst_names_series\n',first_names_series)
print('\nlast_names_series\n',last_names_series)

print('\nDataFrame after adding FirstName and LastName columns')
print(df)