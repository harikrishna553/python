import pandas as pd

# Example 1: Series from List
print('Series from List')
print('---------------------------')

# Get series from a list
primes = [2, 3, 5, 7, 11]
primes_series = pd.Series(primes)

print('primes_series')
print(primes_series)

# Access element by label
element_with_label_2 = primes_series[2]
print('\nelement_with_label_2 :', element_with_label_2)

# Access element by integer position
element_at_index_2 = primes_series.iloc[2]
print('\nelement_at_index_2 :', element_at_index_2)

# Example 2: Series from Dictionary
print('\nSeries from Dictionary')
print('---------------------------')

primes_dictionary = {'first_prime' : 2, 'second_prime' : 3, 'third_prime' : 5}
primes_series = pd.Series(primes_dictionary)
print('\nprimes_series')
print(primes_series)

# Access element by label
element_with_label_third_prime = primes_series['third_prime']
print('\nelement_with_label_third_prime :', element_with_label_third_prime)

# Access element by integer position
element_at_index_2 = primes_series.iloc[2]
print('\nelement_at_index_2 :', element_at_index_2)

# Example 3: Specify index labels explicitly for series derived from the list of elements.
print('\nSeries from List and explicit index')
print('---------------------------')
primes = [2, 3, 5]
primes_index = ['first_prime', 'second_prime', 'third_prime']
primes_series = pd.Series(primes, index=primes_index)
print('\nprimes_series')
print(primes_series)

# Access element by label
element_with_label_third_prime = primes_series['third_prime']
print('\nelement_with_label_third_prime :', element_with_label_third_prime)

# Access element by integer position
element_at_index_2 = primes_series.iloc[2]
print('\nelement_at_index_2 :', element_at_index_2)