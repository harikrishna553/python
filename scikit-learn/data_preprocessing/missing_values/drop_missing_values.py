import pandas as pd
import numpy as np

df = pd.DataFrame({
    'a' : [1, 2, 3, 4, 5, 6, 7],
    'b' : [12.3, np.NAN, 143.45, np.NAN, 34, 56, 109],
    'c' : [True, None, True, False, True, None, False]
})

df_exclude_missing_values = df.dropna()
df_exclude_missing_values_of_col_b = df.dropna(subset=['b'])

print(f'df : \n',df)
print(f'\ndf_exclude_missing_values : \n',df_exclude_missing_values)
print(f'\ndf_exclude_missing_values_of_col_b : \n',df_exclude_missing_values_of_col_b)

# Incase if you want to reflect the changes in actual dataframe, set inplace argument to True
df.dropna(inplace=True)
print(f'\ndf : \n',df)