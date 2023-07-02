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

df['Name'] = df['Name'].str.lower()
df['City'] = df['City'].str.lower()
df['Gender'] = df['Gender'].str.lower()

print('\nDataFrame after lowering the string columns \n', df)