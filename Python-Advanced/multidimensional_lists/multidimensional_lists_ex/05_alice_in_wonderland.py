size = int(input())

matrix = []
tea_bags_count = 0
alice_pos = []

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

for row in range(size):
    line = input().split()

    matrix.append(line)
    if 'A' in line:
        alice_pos = [row, line.index('A')]
        matrix[alice_pos[0]][alice_pos[1]] = '*'


while tea_bags_count < 10:
    command = input()
    row, col = alice_pos[0] + directions[command][0], alice_pos[1] + directions[command][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    symbol = matrix[row][col]

    matrix[row][col] = '*'

    if symbol == 'R':
        break
    elif symbol.isdigit():
        tea_bags_count += int(symbol)

    alice_pos = [row, col]

if tea_bags_count < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*row) for row in matrix]