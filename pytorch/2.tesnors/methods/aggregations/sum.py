import torch

tensor_1 = torch.tensor([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

sum_of_values_1 = torch.sum(tensor_1)

sum_of_values_across_rows = torch.sum(tensor_1, dim=0)
sum_of_values_across_columns = torch.sum(tensor_1, dim=1)

print('sum_of_values_1 : ', sum_of_values_1)
print('sum_of_values_across_rows : ', sum_of_values_across_rows)
print('sum_of_values_across_columns : ', sum_of_values_across_columns)