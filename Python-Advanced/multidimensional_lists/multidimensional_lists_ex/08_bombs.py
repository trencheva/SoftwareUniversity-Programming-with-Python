def index_validator(row, col, rows):
    if 0 <= row <= rows and 0 <= col <= rows:
        return True
    return False



rows = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

bomb_coordinates = ((int(el) for el in values.split(',')) for values in input().split())

targets_coordinates = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 0)
)

for row, col in bomb_coordinates:

    element = matrix[row][col]

    if element <= 0:
        continue

    for x, y in targets_coordinates:
        r, c = row + x, col + y

        if 0 <= r < rows and 0 <= c < rows:
            matrix[r][c] -= element if matrix[r][c] > 0 else 0

alive_cells = [num for row in range(rows) for num in matrix[row] if num > 0]

print(f'Alive cells: {len(alive_cells)}')
print(f'Sum: {sum(alive_cells)}')
[print(*row) for row in matrix]
