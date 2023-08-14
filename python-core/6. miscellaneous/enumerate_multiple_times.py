primes = [2, 3, 5, 7, 11]
enumerated_obj = enumerate(primes)

print('\nIterating over enumerated_obj')
for index, value in enumerated_obj:
    print(f'index : {index}, value : {value}')

print('\nIterating over enumerated_obj again')
for index, value in enumerated_obj:
    print(f'index : {index}, value : {value}')
