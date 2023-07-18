import torch

tensor_1_from_2_to_10 = torch.arange(2, 10)
tensor_2_from_2_to_10 = torch.arange(start=2, end=10)
tensor_3_from_2_to_10 = torch.arange(2, 10, step=1)

print('tensor_1_from_2_to_10 : ', tensor_1_from_2_to_10)
print('tensor_2_from_2_to_10 : ', tensor_2_from_2_to_10)
print('tensor_3_from_2_to_10 : ', tensor_3_from_2_to_10)

tensor_from_20_to_100_step_size_10 = torch.arange(2, 100, 10)
print('tensor_from_20_to_100_step_size_10 : ', tensor_from_20_to_100_step_size_10)