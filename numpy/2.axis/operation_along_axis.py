import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])

sum_along_the_row = np.sum(arr, axis=0)
sum_along_the_column = np.sum(arr, axis=1)

print('sum_along_the_row : ', sum_along_the_row)
print('sum_along_the_column : ', sum_along_the_column)