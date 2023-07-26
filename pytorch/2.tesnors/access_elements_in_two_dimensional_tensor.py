import torch

tensor_1 = torch.arange(1, 10).reshape(3, 3)
print('tensor_1 : \n', tensor_1)

print('Access first row : ', tensor_1[0])
print('Access second row : ', tensor_1[1])
print('Access third row : ', tensor_1[2])

print('\nAccess 2nd row 1st element : ', tensor_1[1][0])
print('Access 2nd row 1st element : ', tensor_1[1, 0])