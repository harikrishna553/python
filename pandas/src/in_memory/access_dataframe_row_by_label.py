import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Ram', 'Joel', 'Gopi', 'Jitendra', "Raj"],
        'Age': [34, 25, 29, 41, 52, 23],
        'City': ['Bangalore', 'Chennai', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Chennai']}

df = pd.DataFrame(data)

# Access the index attribute
index_labels = df.index
print(index_labels)

print("\nTaverse the dataframe using RangIndex")
for index_label in index_labels:
    row = df.loc[index_label]
    print(row, "\n")
