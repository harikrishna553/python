import pandas as pd

primes = [2, 3, 5, 7]
series = pd.Series(primes)

print('Original Data : ')
print(series)

print('\nTotal elements in the series are : ', len(series))
