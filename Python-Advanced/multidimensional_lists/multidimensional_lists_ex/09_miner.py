def find_miner_position():
    for row in range(len(matrix)):
        if 's' in matrix[row]:
            miner_r, miner_c = row, matrix[row].index('s')
            return miner_r, miner_c


def check_indices(row, col):
    if 0 <= row < field_size and 0 <= col < field_size:
        return True
    return False


field_size = int(input())
commands = input().split()

matrix = [input().split() for _ in range(field_size)]

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

total_coal = len([el for row in matrix for el in row if el == 'c'])
current_coal = 0

miner_row, miner_col = find_miner_position()
matrix[miner_row][miner_col] = '*'

for command in commands:

    miner_new_row, miner_new_col = miner_row + directions[command][0], miner_col + directions[command][1]

    if not check_indices(miner_new_row, miner_new_col):
        continue

    miner_row, miner_col = miner_new_row, miner_new_col

    if matrix[miner_row][miner_col] == 'e':
        print(f"Game over! ({miner_row}, {miner_col})")
        break
    elif matrix[miner_row][miner_col] == 'c':
        matrix[miner_row][miner_col] = '*'
        current_coal += 1
        if current_coal == total_coal:
            print(f"You collected all coal! ({miner_row}, {miner_col})")
            break
else:
    print(f"{total_coal - current_coal} pieces of coal left. ({miner_row}, {miner_col})")


