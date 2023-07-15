import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print('Running the tensor on : ', device)

vector = torch.tensor([1, 2, 3])
vector = vector.to(device)
sum_of_elements = vector.sum()

print('sum_of_elements : ', sum_of_elements)