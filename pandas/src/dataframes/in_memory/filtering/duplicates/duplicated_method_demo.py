import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Krishna', 'Joel', "Krishna", "Krishna"],
        'Age': [34, 35, 29, 34, 29, 34, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Hyderabad', 'Bangalore', 'Hyderabad']}

df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

print('\nDuplicated rows')
duplicated_rows_condition = df.duplicated()
duplicated_rows = df[duplicated_rows_condition]
print(duplicated_rows)
