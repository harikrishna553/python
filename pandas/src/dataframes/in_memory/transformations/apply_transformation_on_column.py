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

def to_upper(input_str: str):
    return input_str.upper()

columns_to_update = ['Name', 'City']
for column in columns_to_update:
    df[column] = df[column].apply(to_upper)

print('\nDataFrame after converting the Name and City to uppercase')
print(df)