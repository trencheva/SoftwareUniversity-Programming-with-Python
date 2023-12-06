text = input()

while True:
    command = input().split()
    if command[0] == 'Done':
        break

    action = command[0]
    if action == 'Change':
        char = command[1]
        replacement = command[2]
        text = text.replace(char, replacement)
        print(text)
    elif action == 'Includes':
        substring = command[1]
        if substring in text:
            print(True)
        else:
            print(False)
    elif action == 'End':
        substring = command[1]
        if text.endswith(substring):
            print(True)
        else:
            print(False)
    elif action == 'Uppercase':
        text = text.upper()
        print(text)
    elif action == 'FindIndex':
        char = command[1]
        index = text.index(char)
        print(index)
    elif action == 'Cut':
        start_index = int(command[1])
        count = int(command[2])
        text = text[start_index:start_index + count]
        print(text)
