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

# Sort the data set by ascending order of Year column
new_df = df.sort_index(level=0)
print('\nSort the data set by ascending order of Year column\n',new_df)

new_df = df.sort_index(level='Year')
print('\nSort the data set by ascending order of Year column\n',new_df)

# Sort the data by descending order of the Quarter
new_df = df.sort_index(level=1, ascending=False)
print('\nSort the data by descending order of the Quarter\n',new_df)

new_df = df.sort_index(level='Quarter', ascending=False)
print('\nSort the data by descending order of the Quarter\n',new_df)