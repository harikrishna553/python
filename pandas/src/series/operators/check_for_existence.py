import pandas as pd

countries = ['India', 'Afghanistan', 'Thailand', 'Nepal']
capitals = ['New Delhi', 'Kabul', 'Bangkok', 'Kathmandu']

series = pd.Series(capitals, index=countries)
print('series')
print(series, '\n')

def label_existence_check(country_name):
    if country_name in series:
        print(country_name,' exists in the index labels')
    else:
        print(country_name,' do not exists in the index labels')

def value_existence_check(country_name):
    if country_name in series.values:
        print(country_name,' exists in the series values')
    else:
        print(country_name,' do not exists in the series values')

label_existence_check('India')
label_existence_check('China')
print('\n')
value_existence_check('Kathmandu')
value_existence_check('Beijing')
