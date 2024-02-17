rows, cols = [int(x) for x in input().split(', ')]

my_pos = []
matrix = []

total_items_to_collect = 0
collected_items = 0

for row in range(rows):
    line = input().split()
    matrix.append(line)

    if 'Y' in line:
        my_pos = [row, line.index('Y')]

    for el in line:
        if el in ['C', 'G', 'D']:
            total_items_to_collect += 1

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

items_count = {
    'Christmas decorations': 0,
    'Gifts': 0,
    'Cookies': 0,
}

command = input()

while command != 'End':

    direction = command.split('-')[0]
    steps = int(command.split('-')[1])

    for _ in range(steps):
        matrix[my_pos[0]][my_pos[1]] = 'x'
        r, c = my_pos[0] + directions[direction][0], my_pos[1] + directions[direction][1]

        r = (r + len(matrix)) % len(matrix)
        c = (c + cols) % cols
        my_pos = [r, c]

        if matrix[r][c] == 'C':
            items_count['Cookies'] += 1
            collected_items += 1
        elif matrix[r][c] == 'D':
            items_count['Christmas decorations'] += 1
            collected_items += 1
        elif matrix[r][c] == 'G':
            items_count['Gifts'] += 1
            collected_items += 1

        if collected_items == total_items_to_collect:
            break

        matrix[r][c] = 'x'

    matrix[my_pos[0]][my_pos[1]] = 'Y'

    if collected_items == total_items_to_collect:
        print('Merry Christmas!')
        break

    command = input()

print("You've collected:")
for name, count in items_count.items():
    print(f"- {count} {name}")

[print(*row) for row in matrix]