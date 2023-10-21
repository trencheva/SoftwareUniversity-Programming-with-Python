def shoot_command(targets: list, index, power):
    element = int(targets.pop(index)) - power
    if element > 0:
        targets.insert(index, element)
    return targets


def add_command(targets: list, index, value):
    if 0 <= current_index < len(target_as_integers):
        targets.insert(index, value)
        return targets
    print('Invalid placement!')


def strike_command(targets: list, index, radius):
    if index - radius >= 0:
        if index + radius < len(targets):
            targets.pop(index + radius)
            targets.pop(index)
            targets.pop(index - radius)
            return targets
    print("Strike missed!")


target_as_integers = [target for target in input().split()]
while True:
    command_input = input().split()
    if command_input[0] == 'End':
        target_as_integers = [str(s) for s in target_as_integers]
        print('|'.join(target_as_integers))
        break
    command = command_input[0]
    current_index = int(command_input[1])
    power_value_or_radius = int(command_input[2])

    if command == 'Shoot':
        if 0 <= current_index < len(target_as_integers):
            shoot_command(target_as_integers, current_index, power_value_or_radius)
    elif command == 'Add':
        add_command(target_as_integers, current_index, power_value_or_radius)
    elif command == 'Strike':
        strike_command(target_as_integers, current_index, power_value_or_radius)