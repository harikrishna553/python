def largest_number(list_of_elements):
    if type(list_of_elements) != list:
        raise Exception('input must be a list')
    if list_of_elements is None:
        raise Exception('list is None')

    if len(list_of_elements) == 0:
        return None

    max_element = list_of_elements[0]

    for ele in list_of_elements[1:]:
        if max_element < ele:
            max_element = ele
    return max_element

try:
    input = None
    print('Max number : ', largest_number(input))
except Exception as e:
    print(e)

try:
    input = 'hello'
    print('Max number : ', largest_number(input))
except Exception as e:
    print(e)

input = []
print('Max number : ', largest_number(input))

input = [2]
print('Max number : ', largest_number(input))

input = [2, 30, 5, 6]
print('Max number : ', largest_number(input))

