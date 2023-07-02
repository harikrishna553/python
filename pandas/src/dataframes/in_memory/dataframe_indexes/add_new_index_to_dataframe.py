import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Ram', 'Joel', 'Gopi', 'Jitendra', "Raj"],
        'Age': [34, 25, 29, 41, 52, 23],
        'City': ['Bangalore', 'Chennai', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Chennai']}

df = pd.DataFrame(data)
print("with default index")
print(df)

print("\nwith updated index\n")
df.index = ['a', 'b', 'c', 'd', 'e', 'f']
print(df)

print("\nprint with the index label\n")
for label in df.index:
    print("For the index : ",label)
    print(df.loc[label], "\n")