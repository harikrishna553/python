import numpy as np

employee_basic_details = np.array([
    [1, 'Krishna', 34, 'Male'],
    [2, 'Ram', 37, 'Male'],
    [3, 'Chamu', 33, 'Female'],
    [4, 'Sailu', 35, 'Female']
])

employee_address = np.array([
    [1, 'Bangalore', 'India'],
    [2, 'Bangalore', 'India'],
    [3, 'Chennai', 'India'],
    [4, 'Hyderabad', 'India']
])

print(f'employee_basic_details : \n{employee_basic_details}')
print(f'\nemployee_address : \n{employee_address}')

employee_full_details = np.hstack((employee_basic_details, employee_address[:, 1:]))
print(f'\nemployee_full_details : \n{employee_full_details}')

employee_full_details = np.concatenate((employee_basic_details, employee_address[:, 1:]), axis=1)
print(f'\nemployee_full_details : \n{employee_full_details}')