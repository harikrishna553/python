import torch

# Create two matrices
MATRIX_1 = torch.tensor([[1, 2], [3, 4]])
MATRIX_2 = torch.tensor([[5, 6], [7, 8]])

# Perform element-wise matrix multiplication
MATRIX_MUL_RESULT_1 = torch.mul(MATRIX_1, MATRIX_2)

# Alternatively, you can use C = A * B
MATRIX_MUL_RESULT_2 = MATRIX_1 * MATRIX_2

# Print the result
print('MATRIX_1 \n\n', MATRIX_1)
print('\nMATRIX_2 \n\n', MATRIX_2)
print('\nMATRIX_MUL_RESULT_1 \n\n', MATRIX_MUL_RESULT_1)
print('\nMATRIX_MUL_RESULT_2 \n\n', MATRIX_MUL_RESULT_2)
