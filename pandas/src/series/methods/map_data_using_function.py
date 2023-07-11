import pandas as pd

animals = ['Tiger', 'Lion']
fruits = ['Apple', 'Banana']

def map_keys(key):
    if key in fruits:
        return 'Fruit'
    elif key in animals:
        return 'Animal'
    else:
        return 'not_found'

# Create a Series
series = pd.Series(['Apple', 'Tiger', 'Lion', 'Banana'])

# Map the values of the Series using the mapping dictionary
result = series.map(map_keys)

print('Original seires data')
print(series)

print('\nResult after mapping')
print(result)