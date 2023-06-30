import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Krishna"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Rating': [39, 43, 67, 100, 41, 89]}
df = pd.DataFrame(data)
print('Original DataFrame')
print(df)


def about_me(row):
    name = row[0]
    age = row[1]
    city = row[2]

    about_me = f'I am {name} from {city} and I am {age} years old'
    return about_me

# Add new column AboutMe to the existing data set
df['AboutMe'] = df.apply(about_me, axis='columns')
print('\n',df)
