import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Ram', 'Joel', 'Gopi', 'Jitendra', "Raj"],
        'Age': [34, 25, 29, 41, 52, 23],
        'City': ['Bangalore', 'Chennai', 'Hyderabad', 'Hyderabad', 'Bangalore', 'Chennai']}

df = pd.DataFrame(data)

last_5_rows = df.tail()
print("last_5_rows : \n", last_5_rows)

last_3_rows = df.tail(3)
print("\nlast_3_rows : \n", last_3_rows)

except_first_2_rows = df.tail(-2)
print("\nexcept_first_2_rows : \n", except_first_2_rows)
