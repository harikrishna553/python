import pandas as pd

series = pd.Series(['India', 'China', 'Bangladesh', 'Sri Lanka'], index = ['A', 'B', 'C', 'D'])
join_by_comma = ', '.join(series)
join_by_colon = ': '.join(series)

print('join_by_comma : ', join_by_comma)
print('\njoin_by_colon : ', join_by_colon)