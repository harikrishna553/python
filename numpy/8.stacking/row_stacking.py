import numpy as np

emp1 = np.array([1, 'Krishna', 34, 'Bangalore'])
emp2 = np.array([2, 'Chamu', 33, 'Bangalore'])
emp3 = np.array([3, 'Gopi', 37, 'Hyderabad'])

emps = np.row_stack((emp1, emp2, emp3))

print(f'emps : \n{emps}')