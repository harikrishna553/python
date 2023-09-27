import numpy as np

# Create a 3D NumPy array
array = np.arange(24).reshape(2, 2, 6)
print(f'array :\n{array}')

# Split the array into two sub-arrays along the third axis
split_arrays = np.dsplit(array, 2)

print(f'\nsplit_arrays[0] : \n{split_arrays[0]}')
print(f'\nsplit_arrays[1] : \n{split_arrays[1]}')
