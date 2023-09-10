import pandas as pd

df = pd.DataFrame(
    {
       'a': [1, 2, 3, 4],
        'b': [True, False, True, True],
        'c': [1.23, 4.5, 6.7, 8],
        'd': ['a', 'e', 'i', 'o']
    }
)

numeric_column_names = df.select_dtypes(include=['float64', 'int64']).columns
numeric_data = df[numeric_column_names]

print(f'df : \n{df}')
print(f'\nnumeric_column_names : \n{numeric_column_names}')
print(f'\nnumeric_data : \n{numeric_data}')