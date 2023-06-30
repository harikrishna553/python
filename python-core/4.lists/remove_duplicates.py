list = [2, 3, 5, 4, 2, 3, 2]
unique_numbers = []

for num in list:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)