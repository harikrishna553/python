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

year_2022_quarter_3_results = df.loc[(2022, 3)]
print('\nyear_2022_quarter_3_results\n',year_2022_quarter_3_results)

# Extract Sales column only
year_2022_quarter_3_sales = df.loc[(2022, 3), ['Sales']]
print('\nyear_2022_quarter_3_sales\n',year_2022_quarter_3_sales)