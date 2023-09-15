import numpy as np

arr = np.array([
    [1, 2],
    [3, 4]])

euclidian_norm = np.linalg.norm(arr)
manhattan_norm = np.linalg.norm(arr, 1)
infinity_norm = np.linalg.norm(arr, np.inf)

print(f'arr : {arr}')
print(f'euclidian_norm : {euclidian_norm}')
print(f'manhattan_norm : {manhattan_norm}')
print(f'infinity_norm : {infinity_norm}')