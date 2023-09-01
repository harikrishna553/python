import statistics
import numpy as np

# Create a list of numbers
data = [27, 98, 123, 4, 6, 897, 643]

sorted_data =sorted(data)

# Calculate the median
median = statistics.median(sorted_data)

# Calculate the interquartile range
q1 = np.percentile(sorted_data, 25)
q3 = np.percentile(sorted_data, 75)
iqr = q3 - q1

normalized_data = []
for i in data:
    normalized_value = (i-median)/iqr
    normalized_data.append(normalized_value)

# Print the results
print("median:", median)
print("iqr:", iqr)

print('actual_rating,normalized_rating')
for i in range(len(data)):
    print(data[i], ',', normalized_data[i])
