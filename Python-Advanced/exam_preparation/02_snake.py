size = int(input())

food = 0

matrix = []
snake_pos = []

for row in range(size):
    line = list(input())
    matrix.append(line)

    if 'S' in line:
        snake_pos = [row, line.index('S')]
        matrix[snake_pos[0]][snake_pos[1]] = '.'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while food < 10:
    command = input()
    snake_pos[0], snake_pos[1] = snake_pos[0] + directions[command][0], snake_pos[1] + directions[command][1]

    if not (0 <= snake_pos[0] < size and 0 <= snake_pos[1] < size):
        print("Game over!")
        break

    if matrix[snake_pos[0]][snake_pos[1]] == '*':
        food += 1
    elif matrix[snake_pos[0]][snake_pos[1]] == 'B':
        matrix[snake_pos[0]][snake_pos[1]] = '.'

        for r in range(len(matrix)):
            if 'B' in matrix[r]:
                snake_pos = [r, matrix[r].index('B')]
                break

    matrix[snake_pos[0]][snake_pos[1]] = '.'

else:
    matrix[snake_pos[0]][snake_pos[1]] = 'S'
    print("You won! You fed the snake.")
print(f"Food eaten: {food}")

[print(*row, sep='') for row in matrix]
