import numpy as np

user_details = np.loadtxt('userDetails.csv', comments='#', delimiter=',', skiprows=2, usecols=[0,2,3,4])
print(f'user_details : \n{user_details}')