import torch

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
print('multi_dim_tensor dimension : ', multi_dim_tensor.dim())
size = multi_dim_tensor.size()

first_dimension = size[0]
second_dimension = size[1]
third_dimension = size[2]

print('multi_dim_tensor size : ', multi_dim_tensor.size())
print('first_dimension : ', first_dimension)
print('second_dimension : ', second_dimension)
print('third_dimension : ', third_dimension)