import torch

tensor = torch.tensor([1, 2, 3])
unsqueezed_tensor_on_dim_0 = torch.unsqueeze(tensor, dim=0)
unsqueezed_tensor_on_dim_1 = torch.unsqueeze(tensor, dim=1)

print("\nOriginal tensor :\n", tensor)
print("\nunsqueezed_tensor_on_dim_0 :\n",unsqueezed_tensor_on_dim_0)
print("\nunsqueezed_tensor_on_dim_1 :\n",unsqueezed_tensor_on_dim_1)

# Unsqueezing again
unsqueezed_tensor_on_dim_0_again_on_dim_0 = torch.unsqueeze(tensor, dim=0)
unsqueezed_tensor_on_dim_1_again_on_dim_1 = torch.unsqueeze(tensor, dim=1)
print("\nunsqueezed_tensor_on_dim_0_again_on_dim_0 :\n",unsqueezed_tensor_on_dim_0_again_on_dim_0)
print("\nunsqueezed_tensor_on_dim_1_again_on_dim_1 :\n",unsqueezed_tensor_on_dim_1_again_on_dim_1)