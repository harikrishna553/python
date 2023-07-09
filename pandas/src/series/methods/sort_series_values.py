import pandas as pd

series = pd.Series([12, 31, 5, 7])
ascending_order_series = series.sort_values()
descending_order_series = series.sort_values(ascending=False)

print('series')
print(series)

print('\nascending_order_series')
print(ascending_order_series)

print('\ndescending_order_series')
print(descending_order_series)
