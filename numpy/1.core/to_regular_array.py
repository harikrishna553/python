import numpy as np

ndarray1 = np.array([1, 2, 3])
ndarray2 = np.array([['a', 'b'],
                 ['c', 'd']])

list1 = ndarray1.tolist()
list2 = ndarray2.tolist()

print('ndarray1 : ', ndarray1)
print('Type of ndarray1 : ', type(ndarray1))

print('\nndarray2 : ', ndarray2)
print('Type of ndarray2 : ', type(ndarray2))

print('\nlist1 : ', list1)
print('Type of list1 : ', type(list1))

print('\nlist2 : ', list2)
print('Type of list2 : ', type(list2))