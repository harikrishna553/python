import pandas as pd
import numpy as np

# data can be a Python list, NumPy array, dictionary, scalar value, or another Series.
series_from_list = pd.Series([2, 3, 5, 7])
series_from_list_1 = pd.Series(data=[2, 3, 5, 7])
series_from_numpy_array = pd.Series(np.array([2, 3, 5, 7]))
series_from_dict = pd.Series({'FirstPrime' : 2, 'SecondPrime' : 3, 'ThirdPrime' : 5})
series_from_scalar = pd.Series(2)
series_from_another_series = pd.Series(series_from_list)

print('series_from_list:\n',series_from_list)
print('\nseries_from_list_1:\n',series_from_list_1)
print('\nseries_from_numpy_array:\n',series_from_numpy_array)
print('\nseries_from_dict:\n',series_from_dict)
print('\nseries_from_scalar:\n',series_from_scalar)
print('\nseries_from_another_series:\n',series_from_another_series)