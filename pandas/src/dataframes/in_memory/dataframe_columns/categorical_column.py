import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, 41, 52, 31],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male']}

df = pd.DataFrame(data)

# Add 1000000 rows
rows = []
i = 0
while i < 10000000:
    new_row = {}
    if i % 2 == 0:
        new_row = {'Name': 'Name ' + str(i), 'Age': 28, 'City': 'Bangalore', 'Gender': 'Female'}
    else:
        new_row = {'Name': 'Name ' + str(i), 'Age': 28, 'City': 'Hyderabad', 'Gender': 'Male'}

    rows.append(new_row)
    i = i + 1

df = pd.concat([df, pd.DataFrame(rows)])
df.info()

print('\nChange the Gender to categorical column')
df['Gender'] = df['Gender'].astype("category")
df.info()
