import numpy as np
import pandas as pd

arr = np.array([
    ['Krishna', 35, 'Male'],
    ['Thulasi', 24, 'Female'],
    ['Raj', 41, 'Male']
])
print(f'arr : \n{arr}')

column_names = ['name', 'age', 'gender']
df = pd.DataFrame()
df[column_names] = arr
print(f'\ndf : \n{df}')