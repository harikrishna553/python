import pandas as pd

primes = [2, 3, 5, 7]
series = pd.Series(primes)

print('Original Data : ')
print(series)

all_attrs_and_methods = dir(series)
print(all_attrs_and_methods)
