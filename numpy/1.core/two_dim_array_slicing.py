import numpy as np

arr1 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print(arr1)

third_row = arr1[2]
third_row_with_slicing = arr1[2,:]

print('third_row : \n', third_row)
print('third_row_with_slicing : \n', third_row_with_slicing)

third_column = arr1[:,2]
print('third_column \n', third_column)

every_2nd_element_of_third_column = arr1[::2, 2]
print('every_2nd_element_of_third_column \n', every_2nd_element_of_third_column)