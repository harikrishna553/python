import pandas as pd
import numpy as np

df = pd.DataFrame({
    'a' : [1, 2, 3, 4, 5, 6, 7],
    'b' : [12.3, np.NAN, 143.45, np.NAN, 34, 56, 109],
    'c' : [True, None, True, False, True, None, False]
})

print(f'df : \n',df)

df['b'].fillna(0, inplace=True)
df['c'].fillna(True, inplace=True)

print('\nDataframe after replacing numerical missing values with 0 and boolean values with True')

print(f'df : \n',df)