import torch

random_tensor_1 = torch.rand(2, 3)
random_tensor_2 = torch.rand(2, 3, 4)

print('random_tensor_1 : \n', random_tensor_1)
print('random_tensor_1 data type : ', random_tensor_1.dtype)
print('\nrandom_tensor_2 : \n', random_tensor_2)
print('random_tensor_2 data type : ', random_tensor_2.dtype)

random_tensor_3 = torch.rand(2, 3, dtype=torch.cdouble)
print('\nrandom_tensor_3 : \n', random_tensor_3)
print('random_tensor_3 data type : ', random_tensor_3.dtype)