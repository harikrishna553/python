def pretty_print_dict(dict, indent=0):
    for key, value in dict.items():
        if isinstance(value, dict):
            print(' ' * indent + str(key) + ':')
            pretty_print_dict(value, indent + 4)
        else:
            print(' ' * indent + str(key) + ': ' + str(value))

# Example usage:
address = {'city' : 'Banaglore', 'state' : 'Karnataka', 'country' : 'India'}
employee = {'name' : 'Krishna', 'age' : 34, 'address' : address}

pretty_print_dict(employee)
