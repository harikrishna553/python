import pandas as pd

# Create a Pandas DataFrame
df = pd.DataFrame({'data': [100000, 120000, 150000, 170000, 200000, 700000, 200]})

# Calculate the IQR
Q3 = df['data'].quantile(0.75)
Q1 = df['data'].quantile(0.25)
iqr = Q3 - Q1

print(f'Q1 : {Q1}')
print(f'Q3 : {Q3}')
print(f'iqr : {iqr}')