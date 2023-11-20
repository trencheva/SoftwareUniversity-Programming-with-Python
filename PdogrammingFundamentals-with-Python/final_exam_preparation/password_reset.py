def take_odd_positions(raw_password: str):
    return raw_password[1::2]


def cut(raw_password: str, start_index: int, given_length: int):
    part_to_be_removed = raw_password[start_index:start_index+given_length]
    return raw_password.replace(part_to_be_removed, '', 1)


def substitute(raw_password: str, given_substring: str, given_substitution: str):
    return raw_password.replace(given_substring, given_substitution)


password = input()
while True:
    command = input().split()
    if command[0] == 'Done':
        break
    elif command[0] == 'TakeOdd':
        password = take_odd_positions(password)
        print(password)
    elif command[0] == 'Cut':
        index = int(command[1])
        length = int(command[2])
        password = cut(password, index, length)
        print(password)
    elif command[0] == 'Substitute':
        substring = command[1]
        substitution = command[2]
        if substring in password:
            password = substitute(password, substring, substitution)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")

