import pandas as pd

def print_series(series):
    for idx, label in enumerate(series.index):
        print(f"Index: {idx}, Label: {label}, Value: {series[label]}")

primes_list = [2, 3, 5, 7, 11, 13, 17, 19]
index_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
series = pd.Series(primes_list, index=index_labels)

print_series(series)

# Add new value at index label J
series['I'] = 29
print('\nSeries after adding new entry "I"\n')
print_series(series)