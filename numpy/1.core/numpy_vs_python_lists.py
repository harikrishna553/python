import numpy as np

def add_two_lists(list1, list2):
    result = []

    for i in range(len(list1)):
        result.append(list1[i] + list2[i])

    return result


arr1 = [2, 3, 5, 7]
arr2 = [1, 2, 3, 4]
sum_of_arr1_and_arr2 = add_two_lists(arr1, arr2)

numpy_arr1 = np.array(arr1)
numpy_arr2 = np.array(arr2)
sum_of_numpy_arrays = numpy_arr1 + numpy_arr2

print(f'arr1 : {arr1}')
print(f'arr2 : {arr2}')
print(f'sum_of_arr1_and_arr2 : {sum_of_arr1_and_arr2}')
print(f'\nnumpy_arr1 : {numpy_arr1}')
print(f'numpy_arr2 : {numpy_arr2}')
print(f'sum_of_numpy_arrays : {sum_of_numpy_arrays}')
