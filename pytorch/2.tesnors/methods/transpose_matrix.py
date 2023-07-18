import torch

def print_tensor_details(tensor, label):
    print(label)
    print('Tensor : \n', tensor)
    print('Dimensions : ', tensor.ndim)
    print('Size : ', tensor.size())
    print('\n')


# matrix tensor
matrix = torch.tensor([
    [2, 3, 5, 7],
    [11, 13, 17, 19],
    [4, 6, 8, 10]
])

transposed_matrix = matrix.transpose(dim0=0, dim1=1)

print_tensor_details(matrix, 'matrix')
print_tensor_details(transposed_matrix, 'transposed_matrix')