import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Chamu', 'Joel', 'Gopi', 'Sravya', "Raj"],
        'Age': [34, 25, 29, 41, 52, 23],
        'City': ['Bangalore', 'Chennai', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Male', 'Female', 'Male']}

df = pd.DataFrame(data)
print(df)

group_by_city = df.groupby('City')
count_series_by_group_name = group_by_city.size()

print('\nGroup Name\tTotal Records')
for index_label in count_series_by_group_name.index:
    value = count_series_by_group_name[index_label]
    print(f"{index_label} \t {value}")