import pandas as pd

# Create a sample DataFrame
data = {'Year': [2020, 2020, 2020, 2021, 2021, 2021, 2022, 2022],
        'Quarter': [1, 2, 3, 1, 2, 3, 1, 2],
        'Sales': [100, 150, 115, 120, 180, 90, 130, 160],
        'City': ['Bangalore', 'Bangalore', 'Bangalore', 'Hyderabad', 'Hyderabad', 'Hyderabad', 'Chennai', 'Chennai']
        }
df = pd.DataFrame(data)
print('Original DataFrame\n', df)

# Set Year and Quarter as indexes
df.set_index(['Year', 'Quarter'], inplace=True)
print('\nAfter setting index columns Year and Quarter\n',df)

year_values = df.index.get_level_values('Year')
quarter_values = df.index.get_level_values('Quarter')

print('\nyear_values\n', year_values)
print('\nquarter_values\n', quarter_values)

year_values_using_index = df.index.get_level_values(0)
quarter_values_using_index = df.index.get_level_values(1)

print('\nyear_values_using_index\n', year_values_using_index)
print('\nquarter_values_using_index\n', quarter_values_using_index)
