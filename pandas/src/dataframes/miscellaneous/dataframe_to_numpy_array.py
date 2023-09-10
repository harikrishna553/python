import pandas as pd

df = pd.DataFrame(
    {
        'name': ['Krishna', 'Ram', 'Thulasi'],
        'age': [34, 35, 39],
        'gender': ['Male', 'Male', 'Female']
    }
)

numpy_array = df.to_numpy()

print(f'df : \n{df}')
print(f'\nnumpy_array : \n{numpy_array}')

