import numpy as np

two_dim_arr = np.zeros((2, 3))
three_dim_arr = np.ones((2, 3, 4))
two_dim_arr_empty_values = np.empty((2, 3))
random_two_dim_array = np.random.rand(3,2)

print('two_dim_arr :\n', two_dim_arr)
print('\nthree_dim_arr :\n', three_dim_arr)
print('\ntwo_dim_arr_empty_values :\n', two_dim_arr_empty_values)
print('\nrandom_two_dim_array :\n', random_two_dim_array)