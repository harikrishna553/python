import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Ram', 'Joel', 'Gopi', 'Jitendra', "Raj"],
        'Age': [34, 25, 29, 41, 52, 23],
        'City': ['Bangalore', 'Chennai', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Chennai']}

df = pd.DataFrame(data)
print(df)

# Write dataframe to csv file
df.to_csv('/Users/Shared/csv/demo1.csv')

# Write dataframe to csv file not the index
df.to_csv('/Users/Shared/csv/demo2.csv', index=False)

# Write only Name and Age columns to the csv file
df.to_csv('/Users/Shared/csv/demo3.csv', columns=['Name','Age'])

# Write dataframe to csv file with utf-8 encoding
df.to_csv('/Users/Shared/csv/demo4.csv', encoding = 'utf-8')