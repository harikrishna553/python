import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Rating': [91, 76, 67, 100, 87, 89]}

df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

three_younger_emps = df.nsmallest(3, columns='Age')
print('\nthree_younger_emps : \n', three_younger_emps)

three_younger_emps_by_rating = df.nsmallest(3, columns=['Age', 'Rating'])
print('\nthree_younger_emps_by_rating : \n', three_younger_emps_by_rating)