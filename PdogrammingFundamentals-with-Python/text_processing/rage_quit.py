string_and_numbers = input()
rage_message = ''
current_string = ''
repetition_count = ''
for index in range(len(string_and_numbers)):
    if not string_and_numbers[index].isdigit():
        current_string += string_and_numbers[index].upper()
    else:
        for count in range(index, len(string_and_numbers)):
            if string_and_numbers[count].isdigit():
                repetition_count += string_and_numbers[count]
            else:
                break
        rage_message += current_string * int(repetition_count)
        current_string = ''
        repetition_count = ''

unique_symbols = len(set(rage_message))
print(f'Unique symbols used: {unique_symbols}')
print(rage_message)