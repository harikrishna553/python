import torch

tensor_1 = torch.tensor([2, 3, 5, 7])
tensor_2 = torch.tensor([11, 13, 17, 19])
tensor_3 = torch.tensor([23, 29, 31, 37])

new_tensor_1 = torch.stack([tensor_1, tensor_2, tensor_3], dim=0)
new_tensor_2 = torch.stack([tensor_1, tensor_2, tensor_3], dim=1)

print(f'tensor_1 : {tensor_1}')
print(f'\ntensor_2 : {tensor_2}')
print(f'\ntensor_3 : {tensor_3}')
print(f'\nnew_tensor_1 : \n{new_tensor_1}')
print(f'\nnew_tensor_2 : \n{new_tensor_2}')