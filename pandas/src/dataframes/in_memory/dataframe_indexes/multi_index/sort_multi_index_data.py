import pandas as pd

# Create a sample DataFrame
data = {'Year': [2022, 2022, 2020, 2021, 2021, 2021, 2020, 2022],
        'Quarter': [1, 3, 2, 3, 1, 2, 1, 2],
        'Sales': [100, 150, 115, 120, 180, 90, 130, 160],
        'City': ['Bangalore', 'Bangalore', 'Bangalore', 'Hyderabad', 'Hyderabad', 'Hyderabad', 'Chennai', 'Chennai']
        }
df = pd.DataFrame(data)
print('Original DataFrame\n', df)

# Set Year and Quarter as indexes
df.set_index(['Year', 'Quarter'], inplace=True)
print('\nAfter setting index columns Year and Quarter\n',df)

# Sort the data by ascending order of the Year and Quarter columns
new_df = df.sort_index()
print('\nSort the data set by ascending order of index columns\n',new_df)

# Sort the data by descending order of the Year and Quarter columns
new_df = df.sort_index(ascending=False)
print('\nSort the data set by descending order of index columns\n',new_df)

# Sort the data by ascending order of the Year and descending order Quarter columns
new_df = df.sort_index(ascending=[True,False])
print('\nSort the data by ascending order of the Year and descending order Quarter columns\n',new_df)

# Sort the data by descending order of the Year and ascending order Quarter columns
new_df = df.sort_index(ascending=[False, True])
print('\nSort the data by descending order of the Year and ascending order Quarter columns\n',new_df)