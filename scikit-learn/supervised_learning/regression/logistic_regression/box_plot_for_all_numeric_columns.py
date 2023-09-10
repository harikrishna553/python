import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
df = pd.read_csv('weatherAUS.csv')

numerical_columns = [var for var in df.columns if df[var].dtype != 'O']
# print(len(numerical_columns))

plt.figure(figsize=(14, 14))

rows = 4
cols = 4

for i in range(len(numerical_columns)):
    col_name = numerical_columns[i]
    plt.subplot(rows, cols, i+1)
    fig = df.boxplot(column=col_name)
    fig.set_ylabel(col_name)

plt.show()
