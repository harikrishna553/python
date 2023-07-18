import torch

scalar_tensor = torch.tensor(23)
value = scalar_tensor.item()

print('scalar_tensor : ', scalar_tensor)
print('value : ', value)