import pandas as pd

# Print the content of DataFrameGroupBy object
def print_group_by_result(group_by_object):
    for group_name, group_data in group_by_object:
        print("Group Name:", group_name)
        print(group_data)
        print()


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
print_group_by_result(group_by_city)