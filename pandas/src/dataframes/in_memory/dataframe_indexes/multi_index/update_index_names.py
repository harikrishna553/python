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

df.index.set_names('MyYear', level=0, inplace=True)
df.index.set_names('MyQuarter', level=1, inplace=True)

print('\nAfter updating index column names\n',df)