import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Krishna"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Rating': [39, 43, 67, 100, 41, 89]}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

df.set_index(['City', 'Gender'], inplace=True)
print('\nDataframe after setting the indexes\n', df)

df = df.transpose()
print('\nDataframe after transpose\n', df)

all_names = df.loc['Name']
print('\nall_names\n', all_names)

all_persons_in_bangalore = df.loc[('Name'), ('Bangalore')]
print('\nall_persons_in_bangalore\n', all_persons_in_bangalore)