import pandas as pd
from tabulate import tabulate

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Krishna"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Education': ['Graduate', 'Post Graduate', 'PHD', 'Graduate', 'Graduate', 'Intermediate']}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

table = tabulate(df, headers='keys', tablefmt='pretty')
print('table\n',table)