import torch

tensor1 = torch.tensor([2, 3, 5, 7])
tensor2 = torch.tensor([2.05, 3, 5, 7])
tensor3 = torch.tensor([2, 3, 5, 7], dtype=torch.int32)

print('tensor1 : ', tensor1)
print('tensor1 data type: ', tensor1.dtype)

print('\ntensor2 : ', tensor2)
print('tensor2 data type: ', tensor2.dtype)

print('\ntensor3 : ', tensor3)
print('tensor3 data type: ', tensor3.dtype)