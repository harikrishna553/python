import pandas as pd

series = pd.Series([2, 3, 5, 7])

df = series.to_frame()
print(df)

df = series.to_frame(name='primes')
print('\ndf with column name primes')
print(df)

series = pd.Series([2, 3, 5, 7], index = ['A', 'B', 'C', 'D'])
df = series.to_frame(name='primes')
print('\nSeries with index labels')
print(df)