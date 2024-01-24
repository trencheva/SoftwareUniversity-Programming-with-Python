size = int(input())
matrix = []
bunny_pos = []

best_direction = None
best_path = []
max_collected_eggs = float('-inf')

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

for row in range(size):
    line = input().split()
    matrix.append(line)
    if 'B' in line:
        bunny_pos = [row, line.index('B')]


for name, direction in directions.items():

    collected_eggs = 0
    current_path = []
    cur_bunny_row, cur_bunny_col = bunny_pos[0] + direction[0], bunny_pos[1] + direction[1]

    while 0 <= cur_bunny_row < size and 0 <= cur_bunny_col < size:

        if matrix[cur_bunny_row][cur_bunny_col] == 'X':
            break

        collected_eggs += int(matrix[cur_bunny_row][cur_bunny_col])
        current_path.append([cur_bunny_row, cur_bunny_col])

        cur_bunny_row += direction[0]
        cur_bunny_col += direction[1]

    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_direction = name
        best_path = current_path

print(best_direction)
[print(row) for row in best_path]
print(max_collected_eggs)

