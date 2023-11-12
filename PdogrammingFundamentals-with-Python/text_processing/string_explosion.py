some_string = input()
new_string = ''
explosion_strength = 0

for index in range(len(some_string)):
    if some_string[index] == '>':
        new_string += some_string[index]
        explosion_strength += int(some_string[index + 1])
    elif some_string[index].isdigit():
        explosion_strength -= 1
    else:
        if explosion_strength == 0:
            new_string += some_string[index]
        else:
            explosion_strength -= 1

print(new_string)