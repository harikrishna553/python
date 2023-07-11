import pandas as pd

def print_series(series):
    for idx, label in enumerate(series.index):
        print(f"Index: {idx}, Label: {label}, Value: {series[label]}")

primes_list = [2, 3, 5, 7, 11, 13, 17, 19]
index_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
series = pd.Series(primes_list, index=index_labels)

series_copy = series.copy()
series_copy[0] = 23
series_copy['B'] = 29

print('Series Data : ')
print_series(series)

print('\nSeries Copy Data : ')
print_series(series_copy)