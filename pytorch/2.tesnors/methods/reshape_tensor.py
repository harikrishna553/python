import torch

# matrix tensor
matrix = torch.tensor([
    [2, 3, 5, 7],
    [11, 13, 17, 19],
    [4, 6, 8, 10]
])


def print_tensor_details(tensor, label):
    print(label)
    print('Tensor : \n', tensor)
    print('Dimensions : ', tensor.ndim)
    print('Size : ', tensor.size())
    print('\n')


four_rows_three_columns = matrix.view(4, 3)
two_rows_six_columns = matrix.view(2, 6)
one_row_twelve_columns = matrix.view(1, 12)
three_dimension_tensor = matrix.view(2, 2, 3)

print_tensor_details(matrix, 'matrix')
print_tensor_details(four_rows_three_columns, 'four_rows_three_columns')
print_tensor_details(two_rows_six_columns, 'two_rows_six_columns')
print_tensor_details(one_row_twelve_columns, 'one_row_twelve_columns')
print_tensor_details(three_dimension_tensor, 'three_dimension_tensor')
