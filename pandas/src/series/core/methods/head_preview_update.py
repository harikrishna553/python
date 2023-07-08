import pandas as pd

primes = [2, 3, 5, 7]
series = pd.Series(primes)

print('Original Data : ')
print(series)

print('\nUpdating 1st prime to 11')
first_two_primes = series.head(2)
first_two_primes[0] = 11

print('\nAfter updating\n')
print(series)

