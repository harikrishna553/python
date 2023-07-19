import torch

tensor_1 = torch.tensor([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], dtype=torch.float64)

mean_of_values_1 = torch.mean(tensor_1)

mean_of_values_across_rows = torch.mean(tensor_1, dim=0)
mean_of_values_across_columns = torch.mean(tensor_1, dim=1)

print('mean_of_values_1 : ', mean_of_values_1)
print('mean_of_values_across_rows : ', mean_of_values_across_rows)
print('mean_of_values_across_columns : ', mean_of_values_across_columns)