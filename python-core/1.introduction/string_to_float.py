input_str = input('Enter a string ')
print('input_str : ', input_str, " type : ", type(input_str))

try:
    float_var = float(input_str)
    print('float_var : ', float_var, " type : ", type(float_var))
except ValueError as ve:
    print("input string contain non numeric characters. error : ", ve)