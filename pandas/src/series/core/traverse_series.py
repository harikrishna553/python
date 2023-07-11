import pandas as pd

primes_list = [2, 3, 5, 7]
index_labels = ['A', 'B', 'C', 'D']
series = pd.Series(primes_list, index=index_labels)

# Using for loop and series index attribute.
print('Using for loop and series index attribute.')
for index_label in series.index:
    value = series[index_label]
    print(f"Index: {index_label}, Value: {value}")

# Using enumerate method
print('\nUsing for loop and series index attribute.')
for index_position, index_label in enumerate(series.index):
    print(f"Index: {index_position}, Label: {index_label}, Value: {series[index_label]}")

# Using series items method
print('\nUsing series items method')
for index_label, value in series.items():
    print(f"Index: {index_label}, Value: {value}")