import torch
rand_tensor_1 = torch.rand((2, 1))
rand_tensor_1_squeezed = rand_tensor_1.squeeze()

print(f'rand_tensor_1 : \n{rand_tensor_1}')
print(f'\nrand_tensor_1_squeezed : \n{rand_tensor_1_squeezed}')

rand_tensor_1 = torch.rand((2, 1, 2))
rand_tensor_1_squeezed = rand_tensor_1.squeeze()

print(f'\nrand_tensor_1 : \n{rand_tensor_1}')
print(f'\nrand_tensor_1_squeezed : \n{rand_tensor_1_squeezed}')
