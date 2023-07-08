import pandas as pd

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
series = pd.Series(primes)

print('Original Data : ')
print(series)

last_five_primes = series.tail()
last_three_primes = series.tail(3)

print('\nlast_five_primes')
print(last_five_primes)

print('\nlast_three_primes')
print(last_three_primes)