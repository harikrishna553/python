import pandas as pd

# Series holds element of type int64
primes_list = [2, 3, 5, 7, 11]
primes_series = pd.Series(primes_list)

# Series holds element of type bool
boolean_list = [True, False, False, True]
boolean_series = pd.Series(boolean_list)

# Series holds element of type object
generic_list = ['a', 123, True, 1.34]
generic_series = pd.Series(generic_list)

print('Type of elements in primes_series : ', primes_series.dtype)
print('Type of elements in boolean_series : ', boolean_series.dtype)
print('Type of elements in generic_series : ', generic_series.dtype)