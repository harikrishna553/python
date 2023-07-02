import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna   ', 'Sailu', 'Joel  ', '   kranthi', '   Jitendra', "Kumar"],
        'Hobbies': ['Football,Cricket  ', '    Tennis, cricket   ', '   Trekking, reading books', 'Chess', 'Read Books', 'Cricket']}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

new_data = {}
new_df = pd.DataFrame(data)
new_df['Name'] = df['Name'].str.strip()
new_df['Hobbies'] = df['Hobbies'].str.strip()
print('\nDataFrame after trimming whitespaces\n',new_df)

new_df = pd.DataFrame(data)
new_df['Name'] = df['Name'].str.lstrip()
new_df['Hobbies'] = df['Hobbies'].str.lstrip()
print('\nDataFrame after trimming leading whitespaces\n',new_df)

new_df = pd.DataFrame(data)
new_df['Name'] = df['Name'].str.rstrip()
new_df['Hobbies'] = df['Hobbies'].str.rstrip()
print('\nDataFrame after trimming trailing whitespaces\n',new_df)