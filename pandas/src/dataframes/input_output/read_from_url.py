import pandas as pd

url = 'https://data.cityofnewyork.us/api/views/su38-ur5m/rows.csv'
df = pd.read_csv(url)

print(df.head())