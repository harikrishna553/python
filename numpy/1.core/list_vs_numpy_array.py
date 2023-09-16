import numpy as np
from datetime import datetime

min = 1
max = 10000

arr = range(min, max)
numpy_arr = np.arange(min, max)

start = datetime.now()
c = []
d = []
result1 = []
for i in range(len(arr)):
    c.append(arr[i] ** 2)
    d.append(arr[i] + 10)
    result1.append(c[i] + d[i])
stop = datetime.now()
time_in_microseconds = (stop-start).microseconds
print(f'Time taken by pythons lists : {time_in_microseconds}')

start = datetime.now()
result2 = (numpy_arr ** 2) + (numpy_arr + 10)
stop = datetime.now()
time_in_microseconds = (stop-start).microseconds
print(f'Time taken by numpy arrays : {time_in_microseconds}')

print('Is results equal : ', np.array_equal(result2, np.array(result1)))
