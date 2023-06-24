import numpy as np

arr1 = np.linspace(5, 20)
arr2 = np.linspace(5, 20, 4)
arr3 = np.linspace(5, 20, 4, endpoint=False)

array_with_step_size = np.linspace(5, 20, 4,  endpoint=False, retstep=True)

print('arr1 : ', repr(arr1))
print('\narr2 : ', repr(arr2))
print('\narr3 : ', repr(arr3))
print('\narray_with_step_size : ', repr(array_with_step_size))