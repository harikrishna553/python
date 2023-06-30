import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'kranthi', 'Jitendra', 'Kumar'],
        'Hobbies': ['Football,Cricket', 'Tennis, cricket', 'Trekking, reading books', 'Chess', 'Read Books', 'Cricket']}
df = pd.DataFrame(data)

print('Original DataFrame')
print(df)

df.columns = df.columns.str.upper()
print('\nConverted column to upper case :\n', df)