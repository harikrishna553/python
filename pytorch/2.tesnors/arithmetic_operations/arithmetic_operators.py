import torch

# Arithmetic operations between a tensor and scalar
vector_1 = torch.tensor([10, 20, 30, 40])

vector_1_plus_10 = vector_1 + 10
vector_1_minus_10 = vector_1 - 10
vector_1_product_10 = vector_1 * 10
vector_1_divide_10 = vector_1 / 10

print('Arithmetic operations between a tensor and scalar')
print('vector_1 : ', vector_1)
print('vector_1_plus_10 : ', vector_1_plus_10)
print('vector_1_minus_10 : ', vector_1_minus_10)
print('vector_1_product_10 : ', vector_1_product_10)
print('vector_1_divide_10 : ', vector_1_divide_10)

# Arithmetic operations between two tensors
print('\nArithmetic operations between two tensors')
vector_1 = torch.tensor([10, 20, 30, 40])
vector_2 = torch.tensor([2, 5, 6, 9])

vector_1_plus_vector_2 = vector_1 + vector_2
vector_1_minus_vector_2 = vector_1 - vector_2
vector_1_product_vector_2 = vector_1 * vector_2
vector_1_divide_vector_2 = vector_1 / vector_2

print('\nvector_1 : ', vector_1)
print('vector_2 : ', vector_2)
print('vector_1_plus_vector_2 : ', vector_1_plus_vector_2)
print('vector_1_minus_vector_2 : ', vector_1_minus_vector_2)
print('vector_1_product_vector_2 : ', vector_1_product_vector_2)
print('vector_1_divide_vector_2 : ', vector_1_divide_vector_2)

# Arithmetic operations between a tensor and scalar using built-in methods
print('\nArithmetic operations between a tensor and scalar using built-in methods')
vector_1 = torch.tensor([10, 20, 30, 40])

vector_1_plus_10 = torch.add(vector_1, 10)
vector_1_minus_10 = torch.sub(vector_1, 10)
vector_1_product_10 = torch.mul(vector_1, 10)
vector_1_divide_10 = torch.div(vector_1, 10)

print('vector_1 : ', vector_1)
print('vector_1_plus_10 : ', vector_1_plus_10)
print('vector_1_minus_10 : ', vector_1_minus_10)
print('vector_1_product_10 : ', vector_1_product_10)
print('vector_1_divide_10 : ', vector_1_divide_10)

# Matrix Arithmetic
print('\nMatrix Arithmetic')
MATRIX_1 = torch.tensor([
    [10, 20],
    [30, 40]
])

MATRIX_2 = torch.tensor([
    [1, 2],
    [3, 4]
])

MATRIX_1_PLUS_MATRIX_2 = MATRIX_1 + MATRIX_2
MATRIX_1_MINUS_MATRIX_2 = MATRIX_1 - MATRIX_2
MATRIX_1_PRODUCT_MATRIX_2 = MATRIX_1 * MATRIX_2
MATRIX_1_DIVIDE_MATRIX_2 = MATRIX_1 / MATRIX_2

print('\nMATRIX_1 : \n', MATRIX_1)
print('MATRIX_2 : \n', MATRIX_2)
print('MATRIX_1_PLUS_MATRIX_2 : \n', MATRIX_1_PLUS_MATRIX_2)
print('MATRIX_1_MINUS_MATRIX_2 : \n', MATRIX_1_MINUS_MATRIX_2)
print('MATRIX_1_PRODUCT_MATRIX_2 : \n', MATRIX_1_PRODUCT_MATRIX_2)
print('MATRIX_1_DIVIDE_MATRIX_2 : \n', MATRIX_1_DIVIDE_MATRIX_2)
