import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Ram', 'Ravi', 'Joel', "Joel"],
        'Age': [34, 35, 29, 34, 29, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Hyderabad', 'Bangalore']}

df = pd.DataFrame(data)
print(df)