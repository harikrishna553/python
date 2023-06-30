import numpy as np

arr1 = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

arr_from_b_to_g = arr1[1:7]
arr_from_b_to_till_end = arr1[1:]
arr_from_start_to_f = arr1[:6]
arr_from_b_to_g_step_size_2 = arr1[1:7:2]

print('arr1 : \n', arr1)
print('arr_from_b_to_g : \n', arr_from_b_to_g)
print('arr_from_b_to_till_end : \n', arr_from_b_to_till_end)
print('arr_from_start_to_f : \n', arr_from_start_to_f)
print('arr_from_b_to_g_step_size_2 : \n', arr_from_b_to_g_step_size_2)