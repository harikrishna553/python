import numpy as np

one_dim_arr = np.array([1, 2, 3])
two_dim_arr = np.array([[1, 2, 3, 4],
                        [5, 6, 7, 8]])

# Print shape of the array
print('Shape of one_dim_arr : ', one_dim_arr.shape)
print('Shape of two_dim_arr : ', two_dim_arr.shape)

# Print number of rows and columns
print('\nNumber of rows : ', two_dim_arr.shape[0])
print('Number of columns : ', two_dim_arr.shape[1])

# print dimension of the array
print('two_dim_arr is a ', len(two_dim_arr.shape), ' dimensional array')