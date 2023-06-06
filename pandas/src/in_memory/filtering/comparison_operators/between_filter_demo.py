import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Rating': [81, 76, 67, 100, 87, 89]}

df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

print('\nPersons Rating is in between 81 and 89 using & operator')
rating_greater_or_equal_81 = (df['Rating'] >= 81)
rating_less_than_or_equal_81 = (df['Rating'] <= 89)
final_condition = (rating_greater_or_equal_81 & rating_less_than_or_equal_81)
result = df[final_condition]
print(result)

print('\nPersons Percentage is in between 81 and 89 using between operator')
final_condition = df['Rating'].between(81, 89)
result = df[final_condition]
print(result)