matrix = []
my_pos = []
targets_positions = []
shot_targets = 0
total_targets = 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

for row in range(5):
    matrix.append(input().split())

    if 'A' in matrix[row]:
        my_pos = [row, matrix[row].index('A')]
        matrix[my_pos[0]][my_pos[1]] = '.'

    if 'x' in matrix[row]:
        total_targets += matrix[row].count('x')

for index in range(int(input())):
    tokens = input().split()

    action = tokens[0]
    direction = tokens[1]

    if action == 'move':
        row, col = my_pos[0] + directions[direction][0] * int(tokens[2]), my_pos[1] + directions[direction][1] * int(tokens[2])

        if 0 <= row < 5 and 0 <= col < 5:

            if matrix[row][col] == '.':
                my_pos = [row, col]

    elif action == 'shoot':
        r, c = my_pos[0] + directions[direction][0], my_pos[1] + directions[direction][1]

        while 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] == 'x':
                shot_targets += 1
                matrix[r][c] = '.'
                targets_positions.append([r, c])
                break
            r += directions[direction][0]
            c += directions[direction][1]

    if shot_targets == total_targets:
        print(f"Training completed! All {shot_targets} targets hit.")
        break

if shot_targets != total_targets:
    print(f"Training not completed! {total_targets - shot_targets} targets left.")

[print(row) for row in targets_positions]
