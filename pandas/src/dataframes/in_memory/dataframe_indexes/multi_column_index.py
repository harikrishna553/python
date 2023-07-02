import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Ram', 'Joel', 'Gopi', 'Jitendra', "Raj"],
        'Age': [34, 25, 29, 41, 52, 23],
        'City': ['Bangalore', 'Chennai', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Chennai']}

df = pd.DataFrame(data)
print("with default index")
print(df)

print("\n")
print("with Name as index")

df.set_index(["Name", "City"], inplace=True)
print(df)

# Access row with index ("Krishna", "Bangalore")
print('\nAccess row with index ("Krishna", "Bangalore")')
row = df.loc[("Krishna", "Bangalore")]
print(row)