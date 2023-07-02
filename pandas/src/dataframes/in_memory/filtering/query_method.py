import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Krishna"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Rating': [39, 43, 67, 100, 41, 89]}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

# Get all the persons whose name is Krishna
users_with_name_krishna = df.query('Name == "Krishna"')
print('\nusers_with_name_krishna: \n', users_with_name_krishna)

# Get all the persons whose name is not Krishna
users_with_name_not_krishna = df.query('Name != "Krishna"')
print('\nusers_with_name_not_krishna: \n', users_with_name_not_krishna)

# Get all the persons, whose Age > 34
users_age_greater_than_34 = df.query('Age > 34')
print('\nusers_age_greater_than_34: \n', users_age_greater_than_34)

# Get all the persons whose Age > 34 and City is Bangalore
users_age_greater_34_and_city_is_bangalore = df.query('Age > 34 and City == "Bangalore"')
print('\nusers_age_greater_34_and_city_is_bangalore: \n', users_age_greater_34_and_city_is_bangalore)

# Get all the persons whose Age > 34 or City is Bangalore
users_age_greater_34_or_city_is_bangalore = df.query('Age > 34 or City == "Bangalore"')
print('\nusers_age_greater_34_or_city_is_bangalore: \n', users_age_greater_34_or_city_is_bangalore)

# Get all the persons whose Age is in [34, 55]
users_age_in_34_55 = df.query('Age in [34, 55]')
print('\nusers_age_in_34_55: \n', users_age_in_34_55)

# Get all the persons whose age is not in [34, 55]
users_age_not_in_34_55 = df.query('Age not in [34, 55]')
print('\nusers_age_not_in_34_55: \n', users_age_not_in_34_55)