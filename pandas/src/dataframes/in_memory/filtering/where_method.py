import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Rating': [39, 43, 67, 100, 41, 89]}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

# Get the rows whose city is 'Bangalore'
bangalore_users = df.where(df['City'] == 'Bangalore')
print('\nbangalore_users\n', bangalore_users)

bangalore_users = df.where(df['City'] == 'Bangalore', 'not_matched')
print('\nbangalore_users\n', bangalore_users)

# Get the rows whose age is 34 or Gender is 'Female'
users_age_is_34_or_female = df.where((df['Age'] == 34) | (df['Gender'] == 'Female'), 'not_matched')
print('\nusers_age_is_35_or_female\n', users_age_is_34_or_female)