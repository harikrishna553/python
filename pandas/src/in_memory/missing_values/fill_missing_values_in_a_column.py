import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Ram', 'Joel', 'Gopi', 'Jitendra', "Raj"],
        'Age': [34, np.nan, 29, 41, 52, np.nan],
        'City': ['Bangalore', None, 'Hyderabad', None, 'Bangalore', 'Chennai']}

df = pd.DataFrame(data)
print(df)

df['City'] = df['City'].fillna('not_found')
df['Age'].fillna(0, inplace=True)

print('\nAfter filling missing values')
print(df)