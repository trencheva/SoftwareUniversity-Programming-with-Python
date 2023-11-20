raw_activation_key = input()
command = input()


def is_substring_in_key(raw_key: str, substring:str):
    if substring in raw_key:
        return f"{raw_key} contains {substring}"
    return "Substring not found!"


def flipping_in_string(raw_key: str, upper_or_lower: str, start_index: int, end_index: int):
    changed_part = raw_key[start_index:end_index]
    if upper_or_lower == 'Upper':
        raw_key = raw_key.replace(changed_part, changed_part.upper())
    else:
        raw_key = raw_key.replace(changed_part, changed_part.lower())
    return raw_key


def key_slicing(raw_key: str, start_index: int, end_index: int):
    part_to_be_removed = raw_key[start_index:end_index]
    raw_key = raw_key.replace(part_to_be_removed, '')
    return raw_key


while command != "Generate":

    command = command.split('>>>')
    if command[0] == 'Contains':
        print(is_substring_in_key(raw_activation_key, command[1]))
    elif command[0] == 'Flip':
        raw_activation_key = flipping_in_string(raw_activation_key, command[1], int(command[2]), int(command[3]))
        print(raw_activation_key)
    elif command[0] == 'Slice':
        raw_activation_key = key_slicing(raw_activation_key, int(command[1]), int(command[2]))
        print(raw_activation_key)

    command = input()
print(f'Your activation key is: {raw_activation_key}')

