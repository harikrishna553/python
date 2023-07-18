import torch

# Scalar tensor
scalar = torch.tensor(3.14)

# vector tensor
vector = torch.tensor([2, 3, 5, 7])

# matrix tensor
matrix = torch.tensor([
    [2, 3, 5, 7],
    [11, 13, 17, 19]
])

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

print('type of scalar is : ', type(scalar))
print('type of vector is : ', type(vector))
print('type of matrix is : ', type(matrix))
print('type of multi_dim_tensor is : ', type(multi_dim_tensor))