import pandas as pd

primes = [2, 3, 5]
primes_index = ['first_prime', 'second_prime', 'third_prime']
primes_series = pd.Series(primes, index=primes_index, name='Hold the Prime numbers')

primes_series_values = primes_series.values

print('primes_series_values : ', primes_series_values)
print('type of primes_series_values : ', type(primes_series_values))