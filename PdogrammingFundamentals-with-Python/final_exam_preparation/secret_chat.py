def insert_space(message: str, given_index: int):
    return message[0:given_index] + ' ' + message[given_index::]


def reverse(message: str, some_substring: str):
    result = message.replace(some_substring, '', 1) + some_substring[::-1]
    return result


def change_substring(message: str, some_substring: str, some_replacement: str):
    return message.replace(some_substring, some_replacement)


concealed_message = input()
while True:
    command = input().split(':|:')
    if command[0] == 'Reveal':
        break
    elif command[0] == 'InsertSpace':
        index = int(command[1])
        concealed_message = insert_space(concealed_message, index)
        print(concealed_message)

    elif command[0] == 'Reverse':
        substring = command[1]
        if substring in concealed_message:
            concealed_message = reverse(concealed_message, substring)
            print(concealed_message)
        else:
            print('error')
    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        concealed_message = change_substring(concealed_message, substring, replacement)
        print(concealed_message)

print(f"You have a new text message: {concealed_message}")
