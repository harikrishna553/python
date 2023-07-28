import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
vector = torch.tensor([1, 2, 3])
vector = vector.to(device)
vector_increment_by_10 = vector+10

print('vector : ', vector)
print('vector_increment_by_10 : ', vector_increment_by_10)
