import pandas as pd

series1 = pd.Series([2, 3, 5])
series2 = pd.Series([2, 3, 5, 2])

print('is series1 contain duplicates ? ', series1.is_unique)
print('is series2 contain duplicates ? ', series2.is_unique)