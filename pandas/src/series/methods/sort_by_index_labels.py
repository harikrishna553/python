import pandas as pd

data = [2, 3, 5, 7, 11]
index_labels = ['first_prime', 'second_prime', 'third_prime', 'fourth_prime', 'five_prime']

series = pd.Series(data, index=index_labels)
sort_data_by_index_in_asc = series.sort_index()
sort_data_by_index_in_desc = series.sort_index(ascending=False)

print('series')
print(series)

print('\nsort_data_by_index_in_asc')
print(sort_data_by_index_in_asc)

print('\nsort_data_by_index_in_desc')
print(sort_data_by_index_in_desc)