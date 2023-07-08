import pandas as pd

# Series holds element of type int64
primes_list = [2, 3, 5, 7, 11]
primes_series = pd.Series(primes_list)

empty_series = pd.Series([])

print('Is primes_series empty ? ', primes_series.empty)
print('Is empty_series empty ? ', empty_series.empty)