import torch

def print_tensor_details(tensor, label):
    print(label)
    print('Tensor : \n', tensor)
    print('Dimensions : ', tensor.ndim)
    print('Size : ', tensor.size())
    print('\n')


# vector tensor
vector = torch.tensor([2, 3, 5, 7])
transposed_vector = vector.view(4, 1)

print_tensor_details(vector, 'vector')
print_tensor_details(transposed_vector, 'transposed_vector')