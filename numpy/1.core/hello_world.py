import numpy as np

# Multiplication of two sequences
a = [1, 2, 3, 4, 5, 6, 7]
b = [7, 6, 5, 4, 3, 2, 1]

c = []
for i in range((len(a))):
    c.append(a[i] * b[i])
print(c)

print('\nMultiplication of two ndarrays')
a = np.array([1, 2, 3, 4, 5, 6, 7])
b = np.array([7, 6, 5, 4, 3, 2, 1])
c = a * b
print(c)