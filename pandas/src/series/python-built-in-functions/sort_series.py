import pandas as pd

series = pd.Series([12, 31, 5, 7])

series_in_ascending_order = sorted(series)
series_in_descending_order = sorted(series, reverse=True)

print('series')
print(series)

print('\nseries_in_ascending_order')
print(series_in_ascending_order)

print('\nseries_in_descending_order')
print(series_in_descending_order)