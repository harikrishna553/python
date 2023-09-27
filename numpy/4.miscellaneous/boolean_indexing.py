import numpy as np

# Create a NumPy array
data = np.array(range(1, 7))

# Define a boolean condition
# This results in a boolean array: [False, False, True, False, False, True]
condition = ((data % 3) == 0)

# Apply the condition to filter the data
# This selects elements 3 and 6
filtered_data = data[condition]

print(f'data : {data}')
print(f'condition : {condition}')
print(f'filtered_data : {filtered_data}')
