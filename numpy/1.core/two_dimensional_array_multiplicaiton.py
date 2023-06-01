import numpy as np

a = [
    [1, 2, 3],
    [4, 5, 6]
]

b = [
    [1, 2, 3],
    [4, 5, 6]
]
c = []

# multiplication two lists
for i in range(len(a)):
    temp = []
    for j in range(len(a[0])):
        temp.append(a[i][j] * b[i][j])
    c.append(temp)

print("Multiplicaiton of two lists")
print(c)

a = np.array([(1, 2, 3), (4,5,6)])
b = np.array([(1, 2, 3), (4,5,6)])
c =  a * b
print("\nMultiplicaiton of two ndarrays")
print(c)