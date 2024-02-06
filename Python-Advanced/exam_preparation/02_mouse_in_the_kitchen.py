rows, cols = [int(x) for x in input().split(',')]

cupboard_area = []
mouse_pos = []

cheese = 0

for row in range(rows):
    line = list(input())
    cupboard_area.append(line)

    if 'M' in line:
        mouse_pos = [row, line.index('M')]
        cupboard_area[mouse_pos[0]][mouse_pos[1]] = '*'

    cheese += line.count('C')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

command = input()
while command != 'danger':

    r, c = mouse_pos[0] + directions[command][0], mouse_pos[1] + directions[command][1]

    if not (0 <= r < rows and 0 <= c < cols):
        print("No more cheese for tonight!")
        break

    if cupboard_area[r][c] == '@':
        command = input()
        continue

    mouse_pos = [r, c]

    if cupboard_area[r][c] == 'C':
        cheese -= 1

        if cheese == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif cupboard_area[r][c] == 'T':
        print("Mouse is trapped!")
        break

    cupboard_area[mouse_pos[0]][mouse_pos[1]] = '*'
    command = input()

else:
    if cheese > 0:
        print("Mouse will come back later!")
cupboard_area[mouse_pos[0]][mouse_pos[1]] = 'M'
[print(*row, sep='') for row in cupboard_area]
