size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

command = input().split()
while command[0] != 'END':
    action, row, col, number = command[0], int(command[1]), int(command[2]), int(command[3])

    if 0 <= row < size and 0 <= col < size:

        if action == 'Add':
            matrix[row][col] += number
        elif action == 'Subtract':
            matrix[row][col] -= number
    else:
        print('Invalid coordinates')

    command = input().split()

[print(*row) for row in matrix]
