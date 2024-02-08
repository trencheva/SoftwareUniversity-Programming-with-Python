from core import create_sequence, locate_number

command = input()

while command != "Stop":

    number = int(command.split()[-1])
    if 'Create' in command:

        sequence = create_sequence(number)
        print(*sequence)

    else:
        print(locate_number(number, sequence))

    command = input()
