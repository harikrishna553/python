import pandas as pd

list = [1, 4, 3, 2, 4, 3, 2, 1, 3, 2, 1]
series = pd.Series(list)

value_counts_series = series.value_counts()

# Sort in descending order of the occurrences.
value_counts_series_in_asc = series.value_counts(ascending=True)

# Do not sort
value_counts_series_do_not_sort = series.value_counts(sort=False)

# Relative frequencies
value_counts_series_frequency = series.value_counts(normalize=True)

value_counts_series_frequency_in_percentage = value_counts_series_frequency * 100

print('series')
print(series)

print('\nvalue_counts_series')
print(value_counts_series)

print('\nvalue_counts_series_in_asc')
print(value_counts_series_in_asc)

print('\nvalue_counts_series_do_not_sort')
print(value_counts_series_do_not_sort)

print('\nvalue_counts_series_frequency')
print(value_counts_series_frequency)

print('\nvalue_counts_series_frequency_in_percentage')
print(value_counts_series_frequency_in_percentage)