import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(f'arr : \n{arr}')

print(f'\nAll the array elements : \n{arr[:,:]}')
print(f'\nsecond column data : \n{arr[:,1]}')
print(f'\nthird column data : \n{arr[2,:]}')
print(f'\nsecond and third column data : \n{arr[:,1:3]}')
print(f'\nsecond and third rows data : \n{arr[1:3,:]}')
print(f'\nsecond, third rows and first, second columns  : \n{arr[1:3,0:2]}')
print(f'\nselect first and third column : \n{arr[:, ::2]}')
print(f'\nselect first and third rows : \n{arr[::2, :]}')
print(f'\ninclude second and fourth columns : \n{arr[:, [1, 3]]}')
print(f'\nselect all the rows from column 2 : \n{arr[:, 2:]}')
print(f'\nselect all the columns from row 2: \n{arr[1:, :]}')

# Exclusion examples
print(f'\nexclude from second column onwards : \n{arr[:, :2]}')
print(f'\nexclude from second onwards : \n{arr[:1, :]}')
