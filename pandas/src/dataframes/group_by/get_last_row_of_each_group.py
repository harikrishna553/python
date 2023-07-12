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
data = {'Name': ['Krishna', 'Chamu', 'Joel', 'Gopi', 'Sravya', "Raj"],
        'Age': [34, 25, 29, 41, 52, 23],
        'City': ['Bangalore', 'Chennai', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Male', 'Female', 'Male']}

df = pd.DataFrame(data)
print(df)

group_by_city = df.groupby('City')
print('\nGroup by city is')
print('type of group_by_city is : ', type(group_by_city))
print_group_by_result(group_by_city, 'Group by city details')

last_row_of_each_group = group_by_city.last()
print('\ntype of last_row_of_each_group : ', type(last_row_of_each_group))
print('last of each group are')
print(last_row_of_each_group)
