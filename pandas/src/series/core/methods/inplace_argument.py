import pandas as pd

primes_list = [19, 7, 2, 5, 13, 11, 17, 3]
series = pd.Series(primes_list)

# Sort the series values
series.sort_values()

print('series by not setting inplace argument')
print(series)

# Sort the series values by setting inplace argument to True
series.sort_values(inplace=True)
print('\nseries by setting inplace argument')
print(series)