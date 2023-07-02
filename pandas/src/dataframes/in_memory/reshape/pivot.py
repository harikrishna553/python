import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Krishna"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Education': ['Graduate', 'Post Graduate', 'PHD', 'Graduate', 'Graduate', 'Intermediate']}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

new_df = df.pivot(index=['Education', 'Age'], columns=['City', 'Gender'], values = ['Name'])
print('\nnew_df\n',new_df)