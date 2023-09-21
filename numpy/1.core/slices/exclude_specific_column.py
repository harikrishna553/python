import numpy as np

# Create a sample 2D array
arr = np.array([[1, 2, 3, 4, 5, 6, 7],
                [8, 9, 10, 11, 12, 13, 14],
                [15, 16, 17, 18, 19, 20, 21]])

# Define the column to exclude (0-based index)
col_to_exclude = 3

# Select all the columns upto this columns
arr1 = arr[:, :col_to_exclude]

# Select all the columns from col_to_exclude+1
arr2 = arr[:, col_to_exclude+1:]

new_arr1 = np.concatenate((arr1, arr2), axis=1)
new_arr2 = np.hstack((arr1, arr2))

# Print the new array
print(f'new_arr1 : \n{new_arr1}')
print(f'new_arr2 : \n{new_arr2}')
