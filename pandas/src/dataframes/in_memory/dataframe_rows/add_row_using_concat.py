import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, 41, 52, 31],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male']}
df = pd.DataFrame(data)
print(df)


# Add 2 rows
rows = []
new_row1 = {'Name': 'Ramya', 'Age': 28, 'City': 'Bangalore', 'Gender': 'Female'}
new_row2 = {'Name': 'Sai', 'Age': 38, 'City': 'Bangalore', 'Gender': 'Male'}
rows.append(new_row1)
rows.append(new_row2)

print('\nAdd 2 rows to the DataFrame\n')
df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)
print(df)
