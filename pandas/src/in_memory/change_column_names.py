import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu'],
        'Age': [34, 35, 29, 35],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female'],
        'Rating': [81, 76, 67, 100]}

df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

df.columns = ['User_Name', 'Age', 'City', 'Gender', 'User_Rating']
print('\nDataFrame after renaming the columns')
print(df)