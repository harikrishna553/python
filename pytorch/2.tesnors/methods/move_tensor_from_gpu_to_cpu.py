import torch

# Create a tensor on CUDA
tensor = torch.rand(2, 4).cuda()

# Move the tesnor to CPU
cpu_tensor = tensor.cpu()

print(cpu_tensor)
