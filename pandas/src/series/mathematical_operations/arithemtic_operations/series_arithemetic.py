import pandas as pd

series1 = pd.Series([2, 4, 6, 8])
series2 = pd.Series([1, 3, 5, 7])

addition = series1 + series2
subtraction = series1 - series2
multiplication = series1 * series2
division = series1 / series2

print('series1')
print(series1)

print('\nseries2')
print(series2)

print('\naddition')
print(addition)

print('\nsubtraction')
print(subtraction)

print('\nmultiplication')
print(multiplication)

print('\ndivision')
print(division)