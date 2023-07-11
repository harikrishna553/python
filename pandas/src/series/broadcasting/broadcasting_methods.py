import pandas as pd

primes = [2, 4, 6, 8]
series = pd.Series(primes)

print('Original Data : ')
print(series)

add_by_5 = series.add(5)
subtract_by_5 = series.sub(5)
multiply_by_5 = series.mul(5)
divide_by_5 = series.div(5)

print('\nData after adding the scalar: ')
print(series)

print('\nadd_by_5: ')
print(add_by_5)

print('\nsubtract_by_5: ')
print(subtract_by_5)

print('\nmultiply_by_5: ')
print(multiply_by_5)

print('\ndivide_by_5: ')
print(divide_by_5)