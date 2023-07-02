import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Ram', 'Joel', 'Gopi', 'Jitendra', "Raj"],
        'Age': [34, 25, 29, 41, 52, 23],
        'City': ['Bangalore', 'Chennai', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Chennai']}

df = pd.DataFrame(data)
print(df)

# Add new column Country with value 'India'
print('\nInsert new column Country with value "India" at the location 1')
df.insert(loc=1, column='Country', value='India')
print(df)
