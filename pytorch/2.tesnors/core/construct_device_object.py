import torch

# Create a device object for CPU
device_cpu = torch.device('cpu')

# Create a device object for CUDA
device_cuda_any_available_gpu = torch.device('cuda')
device_cuda_third_gpu = torch.device('cuda:2')

# Print the device objects
print(device_cpu)
print(device_cuda_any_available_gpu)
print(device_cuda_third_gpu)

# Use the device object in tensor construction
vector = torch.tensor([2, 3, 5, 7], device=device_cpu)
print('vector : ', vector)
print('vector device : ', vector.device)