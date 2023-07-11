import pandas as pd
import numpy as np

series1 = pd.Series([0.2, 0.4, 0.6, 0.8, 0.10])
series2 = pd.Series([0.1, 0.3, 0.5, 0.7, 0.11])

correlation_of_series = series1.corr(series2)
covariance_of_series = series1.cov(series2)
percentile_series = series1.quantile(series2)

print('series1')
print(series1)

print('\nseries2')
print(series2)

print('\ncorrelation_of_series')
print(correlation_of_series)

print('\ncovariance_of_series')
print(covariance_of_series)

print('\npercentile_series')
print(percentile_series)