import pandas as pd

country_dataset = {
    'countries' : ['India', 'China', 'Sri Lanka']
}

df = pd.DataFrame(country_dataset)
series = df.squeeze()

print('df : ')
print(df)
print('type of df : ', type(df))

print('\nseries :')
print(series)
print('type of series : ', type(series))