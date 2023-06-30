import pandas as pd

# Create a sample DataFrame
data = {'Title': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Krishna"],
        'Age': [34, 35, 234, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Rating': [67, 43, 67, 100, 41, 89]}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

df['City'] = df['City'].str.replace('Bangalore', 'Mumbai')
print('\nDataFrame after replacing City value Hyderabad to Mumbai\n', df)

# Replace values in multiple columns
replace_dict = {'Krishna': 'Hari', 'Hyderabad': 'Delhi'}
df = df.replace(replace_dict)
print('\nDataframe after replacing the dictionary of values\n', df)