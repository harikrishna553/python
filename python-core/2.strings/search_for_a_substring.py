input_str = 'Hello World'

index = input_str.find('e')
if index != -1:
    print("First occurrence of char 'e' is at index : ", index)
else:
    print("char 'e' is not found")

index = input_str.find('x')
if index != -1:
    print("First occurrence of char 'x' is at index : ", index)
else:
    print("char 'x' is not found")


index = input_str.find('Wor')
if index != -1:
    print("First occurrence of string 'Wor' is at index : ", index)
else:
    print("String 'Wor' is not found")