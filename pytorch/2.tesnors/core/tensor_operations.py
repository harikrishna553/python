import torch

# Reduction operation (sum)
vector_tensor = torch.tensor([2, 3, 5])
sum_of_numbers = torch.sum(vector_tensor)
product_of_numbers = torch.prod(vector_tensor)

print('vector_tensor : ', vector_tensor)
print('sum_of_numbers : ', sum_of_numbers)
print('product_of_numbers : ', product_of_numbers)

# Element wise operation
vector_tensor_1 = torch.tensor([2, 3, 5])
vector_tensor_2 = torch.tensor([7, 11, 13])
addition_of_tensors = vector_tensor_1 + vector_tensor_2

print('\nAddition of elements in two sensors')
print('vector_tensor_1 : ', vector_tensor_1)
print('vector_tensor_2 : ', vector_tensor_2)
print('addition_of_tensors : ', addition_of_tensors)

# Matrix multiplication
matrix_1 = torch.tensor([[1, 2], [3, 4]])
matrix_2 = torch.tensor([[5, 6], [7, 8]])
matrix_multiplication_result = torch.matmul(matrix_1, matrix_2)

print('\nMatrix multiplication')
print('\nmatrix_1 : \n', matrix_1)
print('\nmatrix_2 : \n', matrix_2)
print('\nmatrix_multiplication_result : \n', matrix_multiplication_result)