import pandas as pd

# Create a Series
series = pd.Series(['Apple', 'Tiger', 'Lion', 'Banana'])

# Define a mapping dictionary
mapping = {'Apple': 'Fruit', 'Banana': 'Fruit', 'Tiger': 'Animal', 'Lion' : 'Animal'}

# Map the values of the Series using the mapping dictionary
result = series.map(mapping)

print('Original seires data')
print(series)

print('\nResult after mapping')
print(result)