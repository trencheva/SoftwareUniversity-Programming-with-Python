rows = int(input())
racing_number = input()

matrix = [input().split() for row in range(rows)]

passed_kilometers = 0
car_pos = [0, 0]

reached_the_finish_line = False

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

command = input()
while command != 'End':

    r, c = car_pos[0] + directions[command][0], car_pos[1] + directions[command][1]

    car_pos = [r, c]

    if matrix[r][c] == 'T':
        matrix[r][c] = '.'

        for row in range(rows):
            if 'T' in matrix[row]:
                car_pos = [row, matrix[row].index('T')]

                matrix[car_pos[0]][car_pos[1]] = '.'
                passed_kilometers += 30
                break

    elif matrix[r][c] == 'F':

        print(f"Racing car {racing_number} finished the stage!")
        passed_kilometers += 10
        break

    else:
        passed_kilometers += 10

    command = input()


if command == 'End' and matrix[car_pos[0]][car_pos[1]] == 'C':
    print(f"Racing car {racing_number} finished the stage!")
elif command == 'End':
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {passed_kilometers} km.")

matrix[car_pos[0]][car_pos[1]] = 'C'

[print(*row, sep='') for row in matrix]
