import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'kranthi', 'Jitendra', "Kumar"],
        'Age': [34, 35, 234, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Hobbies': ['Football,Cricket', 'Tennis, cricket', 'Trekking, reading books', 'Chess', 'Read Books', 'Cricket']}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

# Get a boolean series to find the names ends with a (case insensitive)
name_ends_with_a = df['Name'].str.lower().str.endswith('a')
print('\nname_ends_with_a\n', name_ends_with_a)

persons_name_ends_with_a = df[name_ends_with_a]
print('\npersons_name_ends_with_a\n', persons_name_ends_with_a)