import pandas as pd

def print_series(series):
    for idx, label in enumerate(series.index):
        print(f"Index: {idx}, Label: {label}, Value: {series[label]}")

primes_list = [2, 3, 5, 7, 11, 13, 17, 19]
index_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
series = pd.Series(primes_list, index=index_labels)

print_series(series)

# Access elements by index label 'A'
with_label_a = series.get('A')
print('\nwith_label_a : ', with_label_a)

# Access elements by index labels 'A' and 'D'
with_label_a_and_d = series.get(['A', 'D'])
print('\nwith_label_a_and_d : ')
print(with_label_a_and_d)

# Access elements by index position 1
with_index_1 = series.get(1)
print('\nwith_index_1 : ', with_index_1)

# Access elements by index position 1 and 5
with_index_1_and_5 = series.get([1, 5])
print('\nwith_index_1_and_5 : ')
print(with_index_1_and_5)

# Access elements with position or label that do not exists
with_label_do_not_exist = series.get('some_label')
with_index_do_not_exist = series.get(123)
print('\nwith_label_do_not_exist : ', with_label_do_not_exist)
print('\nwith_index_do_not_exist : ', with_index_do_not_exist)

# Supply default values
with_label_do_not_exist = series.get('some_label', 'not_found')
with_index_do_not_exist = series.get(123, 'not_found')
print('\nwith_label_do_not_exist : ', with_label_do_not_exist)
print('\nwith_index_do_not_exist : ', with_index_do_not_exist)

default_values_with_multiple_1 = series.get([21, 5, 143], 'not_found')
default_values_with_multiple_2 = series.get(['A', 'Z', 'Y', 'C'], 'not_found')
print('\ndefault_values_with_multiple_1 : ')
print(default_values_with_multiple_1)
print('\ndefault_values_with_multiple_2 : ')
print(default_values_with_multiple_2)


