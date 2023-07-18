import torch

# Define the matrices A and B
A = torch.tensor([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

B = torch.tensor([[1, 2],
                  [3, 4],
                  [5, 6]])

# Perform matrix multiplication using torch.matmul()
C_1 = torch.matmul(A, B)

# Perform matrix multiplication using @ operator
C_2 = A @ B

print('A\n', A)
print('\nB\n', B)
print('\nC_1\n', C_1)
print('\nC_2\n', C_2)

