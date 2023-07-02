import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Ram', 'Joel', 'Gopi', 'Jitendra', "Raj"],
        'Age': [34, np.nan, 29, 41, 52, np.nan],
        'City': ['Bangalore', None, 'Hyderabad', None, 'Bangalore', 'Chennai']}

df = pd.DataFrame(data)
print(df)

print('\nGet the DataFrame information')
df.info()

if df['Age'].hasnans == True:
    print('\nFound missing values, replacing them with 0')
    df['Age'].fillna(0, inplace=True)

print('\nSet the type of "age" column as int')
df['Age'] = df['Age'].astype('int')
df.info()