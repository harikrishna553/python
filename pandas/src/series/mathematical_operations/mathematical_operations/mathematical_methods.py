import pandas as pd
import numpy as np

series1 = pd.Series([-45, 90, -135, 180, 275, 360])

print('series1')
print(series1)

abs_series = series1.abs()
exponential_series = np.exp(series1)
log_series = np.log(series1.abs())
square_root_series = np.sqrt(series1.abs())
cos_series = np.cos(series1)
sin_series = np.sin(series1)
tan_series = np.tan(series1)

print('\nabs_series')
print(abs_series)

print('\nexponential_series')
print(exponential_series)

print('\nlog_series')
print(log_series)

print('\nabs_series')
print(abs_series)

print('\nsquare_root_series')
print(square_root_series)

print('\ncos_series')
print(cos_series)

print('\nsin_series')
print(sin_series)

print('\ntan_series')
print(tan_series)