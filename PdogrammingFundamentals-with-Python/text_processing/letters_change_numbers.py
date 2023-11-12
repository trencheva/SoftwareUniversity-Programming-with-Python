list_of_strings = [string.strip() for string in input().split()]
total_sum = 0

for current_string in list_of_strings:
    current_number = int(current_string[1:-1])

    if current_string[0].isupper():
        current_number /= ord(current_string[0]) - 64
    elif current_string[0].islower():
        current_number *= ord(current_string[0]) - 96

    if current_string[-1].isupper():
        current_number -= ord(current_string[-1]) - 64
    elif current_string[-1].islower():
        current_number += ord(current_string[-1]) - 96

    total_sum += current_number

print(f'{total_sum:.2f}')