import numpy as np
import torch

tensor = torch.tensor([1, 2, 3, 4, 5])
numpy_array = tensor.numpy()

print('numpy_array : ', numpy_array)
print('tensor : ', tensor)

print('\nUpdating a numpy array do not have any affect on tensor and vice versa')
print('Add 1 to the numpy array and 5 to the tensor')
numpy_array = numpy_array + 1
tensor = tensor + 5

print('numpy_array : ', numpy_array)
print('tensor : ', tensor)