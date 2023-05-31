import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Ram', 'Joel', 'Gopi', 'Jitendra', "Raj"],
        'Age': [34, 25, 29, 41, 52, 23],
        'City': ['Bangalore', 'Chennai', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Chennai']}

df = pd.DataFrame(data, index=[1, 2, 3, 4, 5, 6])
print(df)

print('\nAdd new person details using loc\n')
df.loc[7] = ['Chaitu', 42, 'Nellore']
df.loc[len(df)+1] = ['Ravi', 38, 'Vijayawada']
print(df)