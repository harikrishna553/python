import statistics

# Create a list of numbers
data = [27, 98, 123, 4, 6, 897, 643]

# Calculate the mean
mean = statistics.mean(data)

# Calculate the standard deviation
std_dev = statistics.stdev(data)

normalized_data = []
for i in data:
    normalized_value = (i-mean)/std_dev
    normalized_data.append(normalized_value)

# Print the results
print("mean:", mean)
print("standard deviation:", std_dev)

print('actual_rating,normalized_rating')
for i in range(len(data)):
    print(data[i], ',', normalized_data[i])
