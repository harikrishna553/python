import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Percentage': [81, 76, 67, 100, 87, 89]}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

print('\nPersons staying in the City Bangalore or Cheannai')
interested_cities = ['Bangalore', 'Chennai']
interested_cities_bool_series = df['City'].isin(interested_cities)
interested_rows = df[interested_cities_bool_series]
print(df[interested_cities_bool_series])