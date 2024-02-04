import os

while True:
    command = input().split('-')

    if command[0] == 'End':
        break

    elif command[0] == 'Create':
        with open(f'files/{command[1]}', 'w') as file: pass

    elif command[0] == 'Add':
        with open(f'files/{command[1]}', 'a') as file:
            file.write(f'{command[2]}\n')

    elif command[0] == 'Replace':
        try:
            with open(f'files/{command[1]}', 'r+') as file:
                text = file.read()
                text = text.replace(command[2], command[3])

                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print('An error occurred')

    elif command[0] == 'Delete':
        try:
            os.remove(f'files/{command[1]}')
        except FileNotFoundError:
            print('An error occurred')



