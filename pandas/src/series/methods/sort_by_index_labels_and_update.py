import pandas as pd

data = [2, 3, 5, 7, 11]
index_labels = ['first_prime', 'second_prime', 'third_prime', 'fourth_prime', 'five_prime']

series = pd.Series(data, index=index_labels)
print('series')
print(series)

series.sort_index(inplace=True)
print('\nseries after sorting the data in ascending order of index labels')
print(series)