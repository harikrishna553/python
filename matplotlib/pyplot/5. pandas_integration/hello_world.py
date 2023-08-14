import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('inflation.csv')

plt.plot(df['Year'], df['India'], color='red', label='india', markersize=5, marker='o')
plt.plot(df['Year'], df['China'], color='blue', label='india', markersize=5, marker='x')

plt.show()