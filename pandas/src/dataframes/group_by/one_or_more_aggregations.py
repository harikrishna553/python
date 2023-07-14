import pandas as pd

# Print the content of DataFrameGroupBy object
def print_group_by_result(group_by_object, label):
    print('*'*50)
    print(label,'\n')
    for group_name, group_data in group_by_object:
        print("Group Name:", group_name)
        print(group_data)
        print()
    print('*' * 50)


# Create a sample DataFrame
data = { 'Name': ['Krishna', 'Chamu', 'Joel', 'Gopi', 'Sravya', "Raj"],
         'Age': [34, 25, 29, 41, 52, 23],
        'City': ['Bangalore', 'Chennai', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Male', 'Female', 'Male'],
         'Weight': [74, 58, 85, 87, 63, 79]}

df = pd.DataFrame(data)
print(df)

group_by_city = df.groupby('City')
print('\nGroup by city is')
print('type of group_by_city is : ', type(group_by_city))
print_group_by_result(group_by_city, 'Group by city details')

# specify aggregation for each column separately
agg_result = group_by_city.agg({
    'Age' : 'sum',
    'Weight' : 'mean'
})
print('\nSum on Age column and mean on Weight column')
print(agg_result)

# Specify multiple operations on a column
agg_result = group_by_city.agg({
    'Age' : ['sum', 'size'],
    'Weight' : 'mean'
})

print('\nMultiple operations on a column')
print(agg_result)

group_by_city = df[['Age', 'City', 'Weight']].groupby('City')
agg_result = group_by_city.agg(['sum', 'mean', 'size'])
print('\nMultiple operations on a column')
print(agg_result)