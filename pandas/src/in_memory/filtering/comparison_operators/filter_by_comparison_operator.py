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

print('\nExtract the rows with index 2 and 5')
my_list = [False, False, True, False, False, True]
my_series = pd.Series(my_list)
print(df[my_series])

print('\nExtract the rows where gender is Male')
male_gender_boolean_series = (df['Gender'] == 'Male')
male_gender_rows = df[male_gender_boolean_series]
print(male_gender_rows)

print('\nExtract the rows where Percentage > 85')
percentage_greater_85_boolean_series = (df['Percentage'] > 85)
percentage_greater_85_rows = df[percentage_greater_85_boolean_series]
print(percentage_greater_85_rows)