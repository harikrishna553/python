import torch

# Scalar tensor
scalar = torch.tensor(3.14)
print('scalar dimension : ', scalar.dim())
print('scalar dimension : ', scalar.ndim)
print('scalar size : ', scalar.size())
print('scalar size : ', scalar.shape)
print('type of scalar is : ', type(scalar))

# vector tensor
vector = torch.tensor([2, 3, 5, 7])
print('\nvector dimension : ', vector.dim())
print('vector dimension : ', vector.ndim)
print('vector size : ', vector.size())
print('vector size : ', vector.shape)
print('type of vector is : ', type(vector))

# matrix tensor
matrix = torch.tensor([
    [2, 3, 5, 7],
    [11, 13, 17, 19]
])
print('\nmatrix dimension : ', matrix.dim())
print('matrix dimension : ', matrix.ndim)
print('matrix size : ', matrix.size())
print('matrix size : ', matrix.shape)
print('type of matrix is : ', type(matrix))

# multi dimensional tensor
multi_dim_tensor = torch.tensor([
    [
       [2, 3, 5, 7],
       [11, 13, 17, 19],
       [1, 3, 7, 9]
    ],
    [
       [2, 3, 5, 7],
       [11, 13, 17, 19],
       [4, 5, 6, 7]

    ]
])
print('\nmulti_dim_tensor dimension : ', multi_dim_tensor.dim())
print('multi_dim_tensor dimension : ', multi_dim_tensor.ndim)
print('multi_dim_tensor size : ', multi_dim_tensor.size())
print('multi_dim_tensor size : ', multi_dim_tensor.shape)
print('type of multi_dim_tensor is : ', type(multi_dim_tensor))