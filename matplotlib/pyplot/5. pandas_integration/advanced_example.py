import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('inflation.csv')

for column in df:
    if column != 'Year':
        plt.plot(df['Year'], df[column], marker='.', label=column)

plt.legend()
plt.show()