import torch

tensor_1 = torch.arange(1, 17).reshape(2, 2, 4)
print('tensor_1 : \n', tensor_1)

print('Access first row : \n', tensor_1[0])
print('Access second row : \n', tensor_1[1])

print('\nAccess first element of first row \n', tensor_1[0][0])
print('\nAccess third element of first row of the first row \n', tensor_1[0][0][2])

