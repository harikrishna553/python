import numpy as np

# Set the random seed value to 47
np.random.seed(47)

# Generate a 1D array with 5 random numbers from a standard normal distribution
random_array_1d = np.random.rand(5)

# Generate a 2D array with 3 rows and 4 columns of random numbers
random_array_2d = np.random.rand(3, 4)

# Generate a 3D array with dimensions 3 X 4 X 5
random_array_3d = np.random.rand(3, 4, 5)

print(f'random_array_1d : {random_array_1d}')
print(f'\nrandom_array_2d : \n{random_array_2d}')
print(f'\nrandom_array_3d : \n{random_array_3d}')