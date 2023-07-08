import pandas as pd

primes = [2, 3, 5, 7]
series = pd.Series(primes)

print('Original Data : ')
print(series)

primes_dict = dict(series)
print('primes_dict : ', primes_dict)

index_labels = ['first_prime', 'second_prime', 'third_prime', 'fourth_prime']
series = pd.Series(primes, index_labels)

print('\nOriginal Data : ')
print(series)

primes_dict = dict(series)
print('primes_dict : ', primes_dict)
