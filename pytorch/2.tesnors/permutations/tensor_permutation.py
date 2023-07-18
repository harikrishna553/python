import torch

matrix = torch.tensor([
    [2, 3, 5, 7],
    [11, 13, 17, 19],
    [23, 29, 31, 37]
])

matrix_after_permutation = matrix.permute(1, 0)

print('matrix : \n', matrix)
print('matrix size : \n', matrix.size())

print('\nmatrix_after_permutation : \n', matrix_after_permutation)
print('matrix_after_permutation size : \n', matrix_after_permutation.size())

three_dim_tensor = torch.tensor([
    [
        [2, 3, 5, 7],
        [11, 13, 17, 19],
        [23, 29, 31, 37]
    ],
    [
        [2, 4, 6, 8],
        [12, 14, 16, 18],
        [20, 22, 24, 26]
    ]
])
print('\nthree_dim_tensor : \n', three_dim_tensor)
print('three_dim_tensor size : ', three_dim_tensor.size())

permute_1 = three_dim_tensor.permute(0, 2, 1)
print('\npermute_1 : \n', permute_1)
print('permute_1 size : ', permute_1.size())

permute_2 = three_dim_tensor.permute(1, 2, 0)
print('\npermute_2 : \n', permute_2)
print('permute_2 size : ', permute_2.size())