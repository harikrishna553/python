import torch

tensor_1 = torch.tensor([
    [1, 2, 3],
    [41, -50, 6],
    [7, 8, 19]
], dtype=torch.float64)

max_value_position_across_rows = torch.argmax(tensor_1, dim=0)
max_value_position_across_columns = torch.argmax(tensor_1, dim=1)

print('max_value_position_across_rows : ', max_value_position_across_rows)
print('max_value_position_across_columns : ', max_value_position_across_columns)