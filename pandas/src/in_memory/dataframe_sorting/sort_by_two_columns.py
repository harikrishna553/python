import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Raj"],
        'Age': [34, 35, 29, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Grade': ['A', 'B', 'C', 'A', 'B', 'C']}
df = pd.DataFrame(data)
print(df)

# Sort by City and Grade Ascending
print('\nSorty by City and Grade Ascending')
sort_by_city_and_grade_ascending = df.sort_values(['City', 'Grade'])
print(sort_by_city_and_grade_ascending)

# Sort by City and Grade Descending
print('\nSorty by City and Grade Descending')
sort_by_city_and_grade_descending = df.sort_values(['City', 'Grade'], ascending=False)
print(sort_by_city_and_grade_descending)

# Sort by City in ascending and Grade Descending
print('\nSort by City in ascending and Grade Descending')
sort_by_city_ascending_and_grade_descending = df.sort_values(['City', 'Grade'], ascending=[True, False])
print(sort_by_city_ascending_and_grade_descending)