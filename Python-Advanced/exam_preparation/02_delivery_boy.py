
rows, cols = [int(x) for x in input().split()]
field = []
boy_pos = []
boy_starting_pos = []

boy_left_the_field = False

for row in range(rows):
    line = list(input())
    field.append(line)

    if 'B' in line:
        boy_pos = [row, line.index('B')]
        boy_starting_pos = boy_pos

        field[boy_pos[0]][boy_pos[1]] = '.'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


while True:
    command = input()

    r, c = boy_pos[0] + directions[command][0], boy_pos[1] + directions[command][1]

    if not (0 <= r < rows and 0 <= c < cols):
        print("The delivery is late. Order is canceled.")
        boy_left_the_field = True
        break

    if field[r][c] == '*':
        continue

    elif field[r][c] == 'P':
        field[r][c] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")

    elif field[r][c] == 'A':
        field[r][c] = 'P'
        print("Pizza is delivered on time! Next order...")
        break

    elif field[r][c] == '-':
        field[r][c] = '.'

    boy_pos = [r, c]

if boy_left_the_field:
    field[boy_starting_pos[0]][boy_starting_pos[1]] = ' '
else:
    field[boy_starting_pos[0]][boy_starting_pos[1]] = 'B'

[print(*row, sep='')for row in field]
