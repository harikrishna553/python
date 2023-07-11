import pandas as pd

series = pd.Series([2, 3, 5, 7], index = ['A', 'B', 'C', 'D'])
my_list = series.to_list()

print(my_list)
print('Type of my_list is : ', type(my_list))