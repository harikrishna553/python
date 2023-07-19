import torch

tensor_1 = torch.tensor([
    [1, 2, 3],
    [41, -50, 6],
    [7, 8, 19]
], dtype=torch.float64)

min_of_values = torch.min(tensor_1)

min_of_values_across_rows = torch.min(tensor_1, dim=0)
min_of_values_across_columns = torch.min(tensor_1, dim=1)

print('min_of_values : ', min_of_values)
print('min_of_values_across_rows : ', min_of_values_across_rows.values)
print('min_of_values_across_columns : ', min_of_values_across_columns.values)