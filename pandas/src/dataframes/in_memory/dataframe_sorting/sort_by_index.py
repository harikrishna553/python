import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Grade': ['A', 'B', 'C', 'A', 'B', 'C']}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

print('\nSort the DataFrame by Age')
df = df.sort_values('Age')
print(df)

print('\nSort by index')
df = df.sort_index()
print(df)

print('\nSort by index in descending')
df = df.sort_index(ascending=False)
print(df)