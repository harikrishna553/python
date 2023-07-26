import torch

# Example 1
tensor_1 = torch.tensor([2, 3, 5, 7])
tensor_2 = torch.tensor([11, 13, 17, 19])

# Concatenate along dimension 0 (rows)
concatenated_tensor_on_dim_0 = torch.cat([tensor_1, tensor_2], dim=0)

print("Example 1: concatenated_tensor_on_dim_0:")
print(concatenated_tensor_on_dim_0)

# Example 2
tensor_1 = torch.tensor([[1, 2], [3, 4]])
tensor_2 = torch.tensor([[5, 6], [7, 8], [9, 10]])

# Concatenate along dimension 0 (rows)
concatenated_tensor_on_dim_0 = torch.cat([tensor_1, tensor_2], dim=0)

print("\nExample 2: concatenated_tensor_on_dim_0:")
print(concatenated_tensor_on_dim_0)

# Example 3
tensor_1 = torch.tensor([[1, 2], [3, 4]])
tensor_2 = torch.tensor([[5], [6]])

# Concatenate along dimension 1 (columns)
concatenated_tensor_on_dim_1 = torch.cat([tensor_1, tensor_2], dim=1)

print("\nExample 3: Concatenated tensor:")
print(concatenated_tensor_on_dim_1)