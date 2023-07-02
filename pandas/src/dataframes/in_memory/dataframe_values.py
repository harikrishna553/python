import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Ram', 'Joel', 'Gopi', 'Jitendra', "Raj"],
        'Age': [34, 25, 29, 41, 52, 23],
        'City': ['Bangalore', 'Chennai', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Chennai']}

df = pd.DataFrame(data)

print(df.values)