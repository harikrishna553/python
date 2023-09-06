import pandas as pd
import numpy as np

df = pd.DataFrame({
    'a' : [1, 2, 3, 4, 5, 6, 7],
    'b' : [12.3, np.NAN, 143.45, np.NAN, 34, 56, 109],
    'c' : [True, None, True, False, True, None, False]
})

print(f'df : \n',df)

median_value = df['b'].median()
df['b'].fillna(median_value, inplace=True)
print(f'\nmedian_value for the column b is : {median_value}')

mode_value = df['c'].mode()
df['c'].fillna(mode_value, inplace=True)
print(f'mode_value for the column c is : {mode_value}')

print('\nDataframe after replacing numerical missing values with 0 and boolean values with True')

print(f'df : \n',df)