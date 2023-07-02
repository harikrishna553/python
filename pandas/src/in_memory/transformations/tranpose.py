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

transposed_df_1 = df.T
transposed_df_2 = df.transpose()

print('\ntransposed_df_1\n', transposed_df_1)
print('\ntransposed_df_2\n', transposed_df_2)

all_person_names = transposed_df_1.loc['Name']
print('\nall_person_names\n',all_person_names)

person_names_and_ages = transposed_df_1.loc[['Name', 'Age']]
print('\nperson_names_and_ages\n',person_names_and_ages)