import torch

tensor_1 = torch.arange(1, 10)
print('tensor_1 : ', tensor_1)

print('2nd element in the tensor : ', tensor_1[2])
print('Elements from index 3 to 7 (exclusive): ', tensor_1[3:7])
print('Elements from index 3 to end: ', tensor_1[3:])
print('Elements from starting to index 5 : ', tensor_1[:5])