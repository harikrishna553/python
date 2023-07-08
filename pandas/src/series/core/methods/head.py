import pandas as pd

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
series = pd.Series(primes)

print('Original Data : ')
print(series)

first_five_primes = series.head()
first_three_primes = series.head(3)

print('\nfirst_five_primes')
print(first_five_primes)

print('\nfirst_three_primes')
print(first_three_primes)