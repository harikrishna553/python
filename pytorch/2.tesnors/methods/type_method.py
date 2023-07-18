import torch

tensor_1 = torch.tensor([2, 3, 5, 7])
tensor_1_type = tensor_1.type()

tensor_2 = tensor_1.type(torch.float64)

print('tensor_1 : ', tensor_1)
print('tensor_1 type : ', tensor_1_type)

print('\ntensor_2 : ', tensor_2)
print('tensor_2 type : ', tensor_2.type())
