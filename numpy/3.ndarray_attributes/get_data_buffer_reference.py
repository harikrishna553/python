import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6])

data_buffer = arr1.data

print('Data_buffer : ', data_buffer)
print('Type of data_buffer : ', type(data_buffer))
print('Content of data_buffer : ', data_buffer.tolist())