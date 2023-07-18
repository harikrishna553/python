import torch

available_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
vector = torch.tensor([1, 2, 3], device=available_device)

print('vector : ', vector)
print('vector device : ', vector.device)
