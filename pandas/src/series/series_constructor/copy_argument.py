import pandas as pd

primes_list_1 = [2, 3, 5, 7]
primes_list_2 = [2, 3, 5, 7]

primes_series_1 = pd.Series(primes_list_1)
primes_series_2 = pd.Series(primes_list_2, copy=False)

print('primes_list_1 : ', primes_list_1)
print('primes_list_2 : ', primes_list_2)
print('\nprimes_series_1')
print(primes_series_1)
print('\nprimes_series_2')
print(primes_series_2)

print('\nAdd one more prime to the lists')
primes_list_1[0] = 11
primes_list_2[0] = 11

print('\nprimes_list_1 : ', primes_list_1)
print('primes_list_2 : ', primes_list_2)
print('\nprimes_series_1')
print(primes_series_1)
print('\nprimes_series_2')
print(primes_series_2)