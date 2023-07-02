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

df.set_index(['City', 'Gender', 'Age'], inplace=True)
print('\nDataframe after setting the indexes\n', df)

df = df.swaplevel('Gender', 'Age')
print('\nAfter swapping index levels Gender and Age\n', df)

df = df.swaplevel(0, 2)
print('\nAfter swapping index levels City and Gender\n', df)