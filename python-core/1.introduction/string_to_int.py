input_str = input('Enter a string ')
print('input_str : ', input_str, " type : ", type(input_str))

try:
    int_var = int(input_str)
    print('int_var : ', int_var, " type : ", type(int_var))
except ValueError as ve:
    print("input string contain non numeric characters. error : ", ve)