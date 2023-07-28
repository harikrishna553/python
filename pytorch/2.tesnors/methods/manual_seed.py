import torch

def random_tesnor(seed_value, no_of_elements):
    torch.manual_seed(seed_value)
    return torch.rand(no_of_elements)

seed_value=235711
no_of_elements=5
random_tesnor_1 = random_tesnor(seed_value,no_of_elements)
random_tesnor_2 = random_tesnor(seed_value,no_of_elements)
random_tesnor_3 = random_tesnor(seed_value,no_of_elements)

print('random_tesnor_1 : ', random_tesnor_1)
print('random_tesnor_2 : ', random_tesnor_2)
print('random_tesnor_3 : ', random_tesnor_3)