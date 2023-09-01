data = [27, 98, 123, 4, 6, 897, 643]
min_val = min(data)
max_val = max(data)

normalized_values = []

for i in data:
    normalized_val = (i - min_val) / (max_val - min_val)
    normalized_values.append(normalized_val)

print('actual_value,normalized_value')
for i in range(len(data)):
    print(data[i],',',normalized_values[i])