import pandas as pd

series1 = pd.Series([2, 4, 6, 8])
scalar = 10

addition = series1 + scalar
subtraction = series1 - scalar
multiplication = series1 * scalar
division = series1 / scalar

print('series1')
print(series1)

print('\nscalar : ', scalar)

print('\naddition')
print(addition)

print('\nsubtraction')
print(subtraction)

print('\nmultiplication')
print(multiplication)

print('\ndivision')
print(division)