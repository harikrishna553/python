import torch

tensor_1 = torch.tensor([2, 3, 5, 7])
tensor_2 = torch.tensor([11, 13, 17, 19])

stacked_tensor = torch.stack([tensor_1, tensor_2], dim=0)
cat_tensor = torch.cat([tensor_1, tensor_2], dim=0)

print(f'tensor_1 : {tensor_1}')
print(f'\ntensor_2 : {tensor_2}')
print(f'\nstacked_tensor : \n{stacked_tensor}')
print(f'\ncat_tensor : \n{cat_tensor}')
