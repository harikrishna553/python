import pandas as pd

country_dataset = {
    'countries' : ['India', 'China', 'Sri Lanka'],
    'capitals' : ['New Delhi', 'Beijing', 'Colombo, Sri Jayawardenepura Kotte']
}

df = pd.DataFrame(country_dataset)
df.set_index('countries', inplace=True)
series = df.squeeze()

print('df : ')
print(df)
print('type of df : ', type(df))

print('\nseries :')
print(series)
print('type of series : ', type(series))