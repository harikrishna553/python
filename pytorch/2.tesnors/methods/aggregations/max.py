import torch

tensor_1 = torch.tensor([
    [1, 2, 3],
    [41, -50, 6],
    [7, 8, 19]
], dtype=torch.float64)

max_of_values = torch.max(tensor_1)

max_of_values_across_rows = torch.max(tensor_1, dim=0)
max_of_values_across_columns = torch.max(tensor_1, dim=1)

print('max_of_values : ', max_of_values)
print('max_of_values_across_rows : ', max_of_values_across_rows.values)
print('max_of_values_across_columns : ', max_of_values_across_columns.values)