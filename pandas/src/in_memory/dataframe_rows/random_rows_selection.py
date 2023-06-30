import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Rating': [81, 76, 67, 100, 87, 89]}

df = pd.DataFrame(data)
print('Original DataFrame')
print(df)

# Select one random row
one_random_row = df.sample()
three_random_rows = df.sample(3)
twenty_percent_samples = df.sample(frac=0.2)
forty_five_percen_samples = df.sample(frac=0.45)

random_single_column_1 = df.sample(axis=1)
random_single_column_2 = df.sample(axis='columns')

random_three_column_1 = df.sample(3, axis=1)
random_three_column_2 = df.sample(3, axis='columns')

print('\none_random_row: \n', one_random_row)
print('\nthree_random_rows: \n', three_random_rows)
print('\ntwenty_percent_samples: \n', twenty_percent_samples)
print('\nforty_five_percen_samples: \n', forty_five_percen_samples)
print('\nrandom_single_column_1: \n', random_single_column_1)
print('\nrandom_single_column_2: \n', random_single_column_2)
print('\nrandom_three_column_1: \n', random_three_column_1)
print('\nrandom_three_column_2: \n', random_three_column_2)