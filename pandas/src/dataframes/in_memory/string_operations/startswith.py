import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'kranthi', 'Jitendra', "Kumar"],
        'Age': [34, 35, 234, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Hobbies': ['Football,Cricket', 'Tennis, cricket', 'Trekking, reading books', 'Chess', 'Read Books', 'Cricket']}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

# Get a boolean series to find the names starts with k (case insensitive)
name_starts_with_k = df['Name'].str.lower().str.startswith('k')
print('\nname_starts_with_k\n', name_starts_with_k)

persons_name_starts_with_k = df[name_starts_with_k]
print('\npersons_name_starts_with_k\n', persons_name_starts_with_k)