import pandas as pd

primes = [2, 3, 5]
primes_index = ['first_prime', 'second_prime', 'third_prime']
primes_series = pd.Series(primes, index=primes_index, name='Hold the Prime numbers')

print('Total elements in the primes_series : ', primes_series.size)