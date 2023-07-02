import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'kranthi', 'Jitendra', 'Kumar'],
        'Hobbies': ['Football,Cricket', 'Tennis, cricket', 'Trekking, reading books', 'Chess', 'Read Books', 'Cricket']}
df = pd.DataFrame(data)

# Set the Name column as row label
df.set_index('Name', inplace=True)

print('Original DataFrame')
print(df)

df.index = df.index.str.upper()
print('\nConverted row index labels to upper case :\n', df)