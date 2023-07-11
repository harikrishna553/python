import pandas as pd

def print_series(series):
    for idx, label in enumerate(series.index):
        print(f"Index: {idx}, Label: {label}, Value: {series[label]}")

primes_list = [2, 3, 5, 7, 11, 13, 17, 19]
index_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
series = pd.Series(primes_list, index=index_labels)

print_series(series)

# Overwrite a series value using index position
series[0] = 29

# Overwrite a series value using index label
series['B'] = 31

# Overwrite multiple values using index position
series[[2, 3]] = [37, 41]

# Overwrite multiple values using index labels
series[['E', 'F']] = [43, 51]

print('\nSeries after overriding')
print(series)