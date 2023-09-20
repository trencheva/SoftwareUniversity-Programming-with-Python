first_string = input()
second_string = input()
new_string = first_string
current_string = ''
for current_char in range(len(first_string)):
    left_string = second_string[:current_char + 1]
    right_string = first_string[current_char + 1:]
    current_string = left_string + right_string
    if new_string != current_string:
        print(current_string)
        new_string = current_string