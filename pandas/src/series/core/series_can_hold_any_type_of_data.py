import pandas as pd

# Series of integer values
primes_series = pd.Series([2, 3, 5, 7])

# Series of boolean values
boolean_series = pd.Series([True, False, False, True])

# Series of mixed values
mixed_series = pd.Series(['Hi', 2, True, 5.67])

print('\nprimes_series\n',primes_series)
print('\nboolean_series\n',boolean_series)
print('\nmixed_series\n',mixed_series)