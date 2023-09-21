import numpy as np

employee_details_1 = np.array([
    [1, 'Krishna', 35, 'Male'],
    [2, 'Ram', 36, 'Male'],
    [3, 'Chamu', 33, 'Female'],
    [4, 'Sailu', 37, 'Female']
])

employee_details_2 = np.array([
    [5, 'Gopi', 38, 'Male'],
    [6, 'Bagavath', 45, 'Male']
])

print(f'employee_details_1 : \n{employee_details_1}')
print(f'\nemployee_details_2 : \n{employee_details_2}')

employees_info = np.vstack((employee_details_1, employee_details_2))
print(f'\nemployees_info : \n{employees_info}')

employees_info = np.concatenate((employee_details_1, employee_details_2), axis=0)
print(f'\nemployees_info : \n{employees_info}')