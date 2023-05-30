import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Ram', 'Joel', 'Gopi', 'Jitendra', "Raj"],
        'Age': [34, 25, 29, 41, 34, 25],
        'City': ['Bangalore', 'Chennai', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Chennai']}

df = pd.DataFrame(data)
print(df)

print('\nFind distinct cities in a DataFrame')
distinct_cities = df['City'].value_counts()
print(distinct_cities)
print('type(distinct_cities) : ', type(distinct_cities))

print('\nFind distinct (city, age) in a DataFrame')
city_and_age = ['City', 'Age']
distinct_cities_and_age = df[city_and_age].value_counts()
print(distinct_cities_and_age)
print('type(distinct_cities_and_age) : ', type(distinct_cities_and_age))

print('\nFind distinct (city and age) in a DataFrame in Normalized way')
distinct_cities_and_age_normalized_data = df[city_and_age].value_counts(normalize = True)
print(distinct_cities_and_age_normalized_data)
print('type(distinct_cities_and_age_normalized_data) : ', type(distinct_cities_and_age_normalized_data))

print('\nFind distinct (cities and age) in a DataFrame in Normalized way')
distinct_cities_and_age_normalized_data_in_percent = df[city_and_age].value_counts(normalize = True) * 100
print(distinct_cities_and_age_normalized_data_in_percent)
print('type(distinct_cities_and_age_normalized_data_in_percent) : ', type(distinct_cities_and_age_normalized_data_in_percent))