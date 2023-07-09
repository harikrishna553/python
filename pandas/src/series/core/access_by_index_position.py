import pandas as pd

def print_series(series):
    for idx, label in enumerate(series.index):
        print(f"Index: {idx}, Label: {label}, Value: {series[label]}")

primes_list = [2, 3, 5, 7, 11, 13, 17, 19]
index_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
series = pd.Series(primes_list, index=index_labels)

print_series(series)

# Access elements by index position
first_prime = series[0]
third_prime = series[2]
print('\nfirst_prime : ', first_prime)
print('third_prime : ', third_prime)

# Access the elements using negative inex
last_prime = series[-1]
second_last_prime = series[-2]
print('\nlast_prime : ', last_prime)
print('second_last_prime : ', second_last_prime)

# Select more than one element
first_two_primes = series[[0, 1]]
print('\nfirst_two_primes :')
print(first_two_primes)

# Select elements within range
elements_from_index_2_to_5 = series[2:5]
print('\nelements_from_index_2_to_5 :')
print(elements_from_index_2_to_5)

elements_from_index_2_to_7_step_size_2 = series[2:5:2]
print('\nelements_from_index_2_to_7_step_size_2 :')
print(elements_from_index_2_to_7_step_size_2)

elements_from_index_2 = series[2:]
print('\nelements_from_index_2 :')
print(elements_from_index_2)

elements_till_index_5 = series[:5]
print('\nelements_till_index_5 :')
print(elements_till_index_5)
