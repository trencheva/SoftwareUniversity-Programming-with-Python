rows, cols, = [int(x) for x in input().split()]

playground = []
my_pos = []

moves_made = 0
touched_opponents = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(rows):
    line = input().split()

    playground.append(line)

    if 'B' in line:
        my_pos = [row, line.index('B')]
        playground[my_pos[0]][my_pos[1]] = '-'


while True:
    command = input()

    if command == "Finish":
        break

    r, c = my_pos[0] + directions[command][0], my_pos[1] + directions[command][1]

    if not (0 <= r < rows and 0 <= c < cols):
        continue

    elif playground[r][c] == 'O':
        continue

    elif playground[r][c] == "P":
        touched_opponents += 1
        playground[r][c] = '-'

    my_pos = [r, c]
    moves_made += 1
    if touched_opponents == 3:
        break

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")
