import torch

# matrix tensor
matrix = torch.tensor([
    [2, 3, 5, 7],
    [11, 13, 17, 19],
    [4, 6, 8, 10]
])

print('Matrix : \n', matrix)
print('Dimension : ', matrix.ndim)
print('Size : ', matrix.size())

# Access first row
first_row = matrix[0]
second_row = matrix[1]
third_row = matrix[2]

print('\nfirst_row : ', first_row)
print('second_row : ', second_row)
print('third_row : ', third_row)

# Access first row third element
first_row_third_ele = matrix[0][2]
print('first_row_third_ele : ', first_row_third_ele)
