vector = [2, 3]
scalar = 2

result_vector = []
for index in range(len(vector)):
    result_vector.append(scalar * vector[index])

print(f'vector : {vector}')
print(f'scalar : {scalar}')
print(f'result_vector : {result_vector}')