import pandas as pd

primes = [2, 3, 5, 7, 11, 13, 17]
primes_index = ['A', 'B', 'C', 'D', 'A', 'B', 'A']
primes_series = pd.Series(primes, index=primes_index)

print('primes_series')
print(primes_series)

associated_with_index_a = primes_series['A']
print('\nassociated_with_index_a')
print(associated_with_index_a)
print('\ntype of associated_with_index_a', type(associated_with_index_a))

associated_with_index_c = primes_series['C']
print('\nassociated_with_index_c')
print(associated_with_index_c)
print('\ntype of associated_with_index_c', type(associated_with_index_c))