import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Ram', 'Joel', 'Gopi', 'Jitendra', 'Raj'],
        'Age': [34, 25, 29, 41, 52, 23],
        'City': ['Bangalore', 'Chennai', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Chennai']}

df = pd.DataFrame(data)
axes = df.axes

row_axes = axes[0]
column_axes = axes[1]

# Traverse the DataFrame rows
print("Traverse data frame by rows")
for row_index in row_axes:
    print(df.iloc[row_index])

# Traverse the DataFrame using index and column access
print("\nTraverse the DataFrame using index and column access")
for i in range(len(df)):
    row = df.iloc[i]
    for column in column_axes:
        print(column, " : ", row[column])
    print("\n")