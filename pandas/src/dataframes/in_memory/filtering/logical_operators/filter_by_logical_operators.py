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

print('\nGet all the students whose Gender is "Male" and Rating is > 45')
gender_male_boolean_series = (df['Gender'] == 'Male')
rating_is_greater_45 = (df['Rating'] > 45)
mask = (gender_male_boolean_series & rating_is_greater_45)
result = df[mask]
print(result)

print('\nGet all the students whose Gender is "Male" or Rating is > 45')
mask = (gender_male_boolean_series | rating_is_greater_45)
result = df[mask]
print(result)

print('\nGet all the persons whose city is not Bangalore.')
mask = ~(df['City'] == 'Bangalore')
result = df[mask]
print(result)