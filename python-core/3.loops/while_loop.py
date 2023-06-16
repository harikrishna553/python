i = 0
while i < 5:
    print('i = ', i)
    i = i + 1
else:
    print('While loop executed successfully')

print('\nTrying while loop with break statement')
i = 0
while i < 5:
    print('i = ', i)
    i = i + 1
    if i == 4:
        print('Exiting the loop, else block will not get called')
        break
else:
    print('While loop executed successfully')
