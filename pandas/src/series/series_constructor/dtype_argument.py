import pandas as pd

data = [2, 3, 5, 7]
index = ['first_prime', 'second_prime', 'third_prime', 'fourth_prime']
series1 = pd.Series(data, index)
series2 = pd.Series(data, index, dtype='float64')

print(series1,'\n')
print(series2)