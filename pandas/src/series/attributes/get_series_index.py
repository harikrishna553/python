import pandas as pd

primes = [2, 3, 5]
primes_index = ['first_prime', 'second_prime', 'third_prime']
primes_series = pd.Series(primes, index=primes_index)

print('primes_series')
print(primes_series, '\n')
print('index_labels of primes_series is ', primes_series.index)

even_numbers = [2, 4, 6, 8]
even_numbers_series = pd.Series(even_numbers)
print('\neven_numbers_series')
print(even_numbers_series, '\n')
print('index_labels of even_numbers_series is ', even_numbers_series.index)