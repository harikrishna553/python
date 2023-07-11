import pandas as pd

primes = [2, 4, 6, 8]
series = pd.Series(primes)

print('Original Data : ')
print(series)

series = series + 5
print('\nData after adding the scalar: ')
print(series)