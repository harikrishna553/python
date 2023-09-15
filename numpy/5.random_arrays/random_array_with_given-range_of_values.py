import numpy as np

def rand_array(a, b, *more):
    return a + (b - a) * np.random.rand(*more)

# Generate a 1D array with 11 random numbers, where values are in range of 5 and 10
random_array_1d = rand_array(5, 10, 11)

# Generate a 2D array with 3 rows and 5 columns, where values are in range of 5 and 10
random_array_2d = rand_array(5, 10, 3, 5)

print(f'random_array_1d : {random_array_1d}')
print(f'\nrandom_array_2d : \n{random_array_2d}')