import json
def pretty_print_dict(dict, indent=0):
   return json.dumps(dict, indent=4)

# Example usage:
address = {'city' : 'Banaglore', 'state' : 'Karnataka', 'country' : 'India'}
employee = {'name' : 'Krishna', 'age' : 34, 'address' : address}

print(pretty_print_dict(employee))
