import pandas as pd

data = [2, 3, 5, 7]
index = ['first_prime', 'second_prime', 'third_prime', 'fourth_prime']
series = pd.Series(data, index)

print(series)