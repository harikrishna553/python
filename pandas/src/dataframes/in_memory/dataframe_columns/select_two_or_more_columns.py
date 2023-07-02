import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Ram', 'Joel', 'Gopi', 'Jitendra', "Raj"],
        'Age': [34, 25, 29, 41, 52, 23],
        'City': ['Bangalore', 'Chennai', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Chennai']}

df = pd.DataFrame(data)
print(df)

print('\nSelect Name and City columns')
two_columns = ['Name', 'City']
name_and_city = df[two_columns]
print(name_and_city)

print('\ntype of name_and_city : ', type(name_and_city))

