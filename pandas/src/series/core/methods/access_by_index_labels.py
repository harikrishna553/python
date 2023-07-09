import pandas as pd

def print_series(series):
    for idx, label in enumerate(series.index):
        print(f"Index: {idx}, Label: {label}, Value: {series[label]}")

primes_list = [2, 3, 5, 7, 11, 13, 17, 19]
index_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
series = pd.Series(primes_list, index=index_labels)

print_series(series)

# Access elements by index label
third_prime = series['C']
print('\nthird_prime : ', third_prime)

# Access elements by index labels
third_and_fourth_primes = series[['C', 'D']]
print('\nthird_and_fourth_primes :')
print(third_and_fourth_primes)
