import pandas as pd

data1 = { 'Name': ['Krishna', 'Chamu', 'Joel'],
         'Age': [34, 25, 29],
        'City': ['Bangalore', 'Chennai', 'Hyderabad'],
        'Gender': ['Male', 'Female', 'Male'],
         'Weight': [74, 58, 85]}

data2 = { 'Name': ['Gopi', 'Sravya', "Raj"],
         'Age': [41, 52, 23],
        'City': ['Hyderabad', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male'],
         'Weight': [87, 63, 79]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print('df1')
print(df1)

print('\ndf2')
print(df2)

final_df = pd.concat([df1, df2])
print('\nDataframe after concatenating df1 and df2 data')
print(final_df)

final_df = pd.concat([df1, df2], ignore_index=True)
print('\nDataframe after concatenating df1 and df2 data by ignoring index')
print(final_df)
