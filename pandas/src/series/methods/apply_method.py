import pandas as pd

list = [1, 2, 3, 4, 5]
series = pd.Series(list)

def square(num):
    return num * num

square_of_the_series = series.apply(square)

print('\nseries')
print(series)

print('\nsquare_of_the_series')
print(square_of_the_series)