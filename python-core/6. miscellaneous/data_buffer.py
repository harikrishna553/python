import array

# Create an array of 32-bit integers
my_buffer = array.array('i', [1, 2, 3, 4, 5])

# Access elements in the buffer
element = my_buffer[2]
print('element at location 2 is : ', element)

# Modify an element in the buffer
my_buffer[1] = 99
print(my_buffer)  # Output: array('i', [1, 99, 3, 4, 5])
