import torch

tensor_1 = torch.tensor([-12, 2, 3, 41, 32, 18, 91, 7])
print('tensor_1 : ', tensor_1)

mask_for_greater_5 = tensor_1 > 5
print('mask_for_greater_5 : ', mask_for_greater_5)
print('elements greater than 5 are  : ', tensor_1[mask_for_greater_5])

mask_for_even_numbers = ((tensor_1 % 2) == 0)
print('mask_for_even_numbers : ', mask_for_even_numbers)
print('even elements in the tensor : ', tensor_1[mask_for_even_numbers])