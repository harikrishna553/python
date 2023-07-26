import torch

tensor_1 = torch.tensor([
    [2, 3, 5, 7],
    [11, 13, 17, 19]
])

tensor_2 = tensor_1.reshape(4, 2)

print(f'tensor_1 : \n{tensor_1}')
print(f'\ntensor_2 : \n{tensor_2}')

# Update the value of tensor_2
tensor_2[0, 1] = 1234567

print('\nUpdating the value of tensor_2')
print(f'\ntensor_1 : \n{tensor_1}')
print(f'\ntensor_2 : \n{tensor_2}')