import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Ram', 'Joel'],
        'Age': [34, 25, 29],
        'City': ['Bangalore', 'Chennai', 'Hyderabad']}

df = pd.DataFrame(data)

# Get the total number of rows using the shape attribute
total_rows = df.shape[0]
print("total_rows : ", total_rows)

# Get the total number of rows using the len function
total_rows = len(df)
print("total_rows : ", total_rows)
