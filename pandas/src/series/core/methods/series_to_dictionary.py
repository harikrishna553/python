import pandas as pd

series = pd.Series([2, 3, 5, 7], index = ['A', 'B', 'C', 'D'])
my_dict = series.to_dict()

print(my_dict)
print('Type of my_dict is : ', type(my_dict))