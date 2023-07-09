import pandas as pd

series = pd.Series([12, 31, 5, 7])
print('series')
print(series)

series.sort_values(inplace=True)
print('\nseries after sorting the values in ascending order')
print(series)
