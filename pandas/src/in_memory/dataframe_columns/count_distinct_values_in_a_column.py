import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Krishna"],
        'Age': [34, 35, 234, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Rating': [67, 43, 67, 100, 41, 89]}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

distinct_column_values = df.nunique()
print('\ndistinct_values\n', distinct_column_values)

print('\nTotal distinct names : ', distinct_column_values['Name'])
print('Total distinct ages : ', distinct_column_values['Age'])
print('Total distinct cities : ', distinct_column_values['City'])
print('Total distinct genders : ', distinct_column_values['Gender'])
print('Total distinct ratings : ', distinct_column_values['Rating'])