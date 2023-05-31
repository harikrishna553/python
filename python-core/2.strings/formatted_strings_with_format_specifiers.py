from datetime import datetime

print('Alignment and padding example')
name = 'Krishna'
age = 35
country = 'India'
msg = f'name : {name:<15}, age : {age:03}, country : {country:>10}.'
print(msg)

print('\nDecimal places example')
pi = 3.1415714285
formatted_pi = f"pi = {pi:.4f}"
print('pi : ', pi)
print('formatted_pi : ', formatted_pi)

print('\nFormat numeric values with a ,')
n = 123456789.987654
formatted_n = f"n = {n:,f}"
print('n : ', n)
print('formatted_n : ', formatted_n)

print('\nFormat numeric values with a , and restrict decimal places to 3')
formatted_n = f"n = {n:,.3f}"
print('formatted_n : ', formatted_n)

print('\nFormat a decimal number to binary, ocatal and hexa')
n = 23
binary = f"Binary: {n:b}"
octal = f"Octal: {n:o}"
hexadecimal = f"Hexadecimal: {n:x}"
print('n : ', n)
print(binary)
print(octal)
print(hexadecimal)

print('\nFormat date and time')
now = datetime.now()
formatted_date_and_time = f"date and time: {now:%Y-%m-%d %H:%M:%S}"
print(formatted_date_and_time)

