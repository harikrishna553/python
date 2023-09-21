import numpy as np

# Create a sample 2D array
arr = np.array([[1, 2, 3, 4, 5, 6, 7],
                [8, 9, 10, 11, 12, 13, 14],
                [15, 16, 17, 18, 19, 20, 21]])

# Define the column to exclude (0-based index)
col_to_exclude = [3]
result = np.delete(arr, col_to_exclude, axis=1)

print(f'arr :\n{arr}')
print(f'\nresult :\n{result}')