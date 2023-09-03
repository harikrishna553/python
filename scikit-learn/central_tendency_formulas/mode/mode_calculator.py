def calculate_mode(data_points):
    # Create a dictionary to count the occurrences of each value
    data_points_count = {}

    # Initialize the maximum count
    max_count = 0

    # Initialize the mode list
    mode_list = []

    for value in data_points:
        if value in data_points_count:
            data_points_count[value] += 1
        else:
            data_points_count[value] = 1

        # Update the maximum count
        if data_points_count[value] > max_count:
            max_count = data_points_count[value]

    # Find all values with the maximum count (modes)
    for key, value in data_points_count.items():
        if value == max_count:
            mode_list.append(key)

    return mode_list


data = [1, 2, 2, 3, 4, 4, 4, 5, 2]

# Calculate the mode(s)
modes = calculate_mode(data)

print("Modes:", modes)
