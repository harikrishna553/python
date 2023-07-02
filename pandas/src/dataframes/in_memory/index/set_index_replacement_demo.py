import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Ram', 'Ravi', 'Joel', "Joel"],
        'Age': [34, 35, 29, 34, 29, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Hyderabad', 'Bangalore']}

df = pd.DataFrame(data)
print(df)

df.set_index(keys=['Name'], inplace=True)
print('\nDataFrame after setting the index to "Name" column')
print(df)

print('\nResetting index')
df.reset_index(inplace=True)
print(df)

df.set_index(keys=['Age'], inplace=True)
print('\nDataFrame after setting the index to "Age" column')
print(df)