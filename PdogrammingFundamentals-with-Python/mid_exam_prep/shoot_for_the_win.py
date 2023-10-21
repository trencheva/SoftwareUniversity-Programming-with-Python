targets_as_integers = [int(s) for s in input().split()]
input_line = input()
while input_line != 'End':
    index = int(input_line)
    if 0 <= index < len(targets_as_integers):
        if targets_as_integers[index] != -1:
            number = targets_as_integers[index]
            for current_target in range(len(targets_as_integers)):
                if targets_as_integers[current_target] != -1:
                    if targets_as_integers[current_target] > number:
                        targets_as_integers[current_target] -= number
                    else:
                        targets_as_integers[current_target] += number

            targets_as_integers[index] = -1

    input_line = input()
shot_targets = targets_as_integers.count(-1)
targets_as_integers = [str(s) for s in targets_as_integers]
print(f"Shot targets: {shot_targets} -> {' '.join(targets_as_integers)}")
