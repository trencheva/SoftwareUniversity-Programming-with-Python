integers_input_as_string = input().split()
integers_input = []
for number in integers_input_as_string:
    integers_input.append(int(number))

while True:
    input_line = input().split()
    command = input_line[0]
    if command == 'end':
        break
    elif command == 'decrease':
        decreased_elements = []
        for element in integers_input:
            decreased_elements.append(element - 1)
        integers_input = decreased_elements
    else:
        first_index = int(input_line[1])
        second_index = int(input_line[2])
        if command == 'swap':
            integers_input[first_index], integers_input[second_index] = integers_input[second_index], integers_input[first_index]
        elif command == 'multiply':
            integers_input[first_index] = integers_input[first_index] * integers_input[second_index]
new_string = []
for num in integers_input:
    new_string.append(str(num))
print(', '.join(new_string))

