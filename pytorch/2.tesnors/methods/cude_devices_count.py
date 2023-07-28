import torch

cuda_devices_count = torch.cuda.device_count()

if cuda_devices_count > 0:
  print(f'There are {cuda_devices_count} CUDA devices available.')
else:
  print("There are no CUDA devices available.")
