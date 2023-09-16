import numpy as np

arr_2d = np.array([
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
])

print(f'arr_2d : \n{arr_2d}')
print(f'Element at row 0 and column 2 is {arr_2d[0, 2]}')
print(f'Element at row 2 and column 0 is {arr_2d[2, 0]}')
print(f'second column elements {arr_2d[:, 2]}')
print(f'second row elements {arr_2d[2, :]}')

arr_3d = np.array([
    [
        (10, 11, 12),
        (100, 101, 102),
        (1000, 1001, 1002)

    ],
    [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    ]
])

print(f'\narr_3d : \n{arr_3d}')
print(f'Element at depth 1, row 0, column 2 : {arr_3d[1, 0, 2]}')
print(f'Element at depth 0, row 2, column 1 : {arr_3d[0, 2, 1]}')