import torch

# Scalar tensor
pi = torch.tensor(3.14)

# vector tensor
v = torch.tensor([2, 3, 5, 7])

# matrix tensor
MATRIX = torch.tensor([
    [2, 3, 5, 7],
    [11, 13, 17, 19]
])

# multi dimensional tensor
MULTI_DIM_TENSOR = torch.tensor([
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

print('type of scalar is : ', type(pi))
print('type of vector is : ', type(v))
print('type of matrix is : ', type(MATRIX))
print('type of multi_dim_tensor is : ', type(MULTI_DIM_TENSOR))