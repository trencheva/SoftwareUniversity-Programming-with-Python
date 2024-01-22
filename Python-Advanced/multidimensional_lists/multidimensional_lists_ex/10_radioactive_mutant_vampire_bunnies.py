def find_player_position():
    for row in range(rows):
        if 'P' in matrix[row]:
            player_r, player_c = row, matrix[row].index('P')
            return player_r, player_c


def check_indices(row, col, player=False):
    global won
    if 0 <= row < rows and 0 <= col < cols:
        return True

    if player:
        won = True


def find_bunnies_positions():
    bunnies_positions = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 'B':
                bunnies_positions.append([row, col])
    return bunnies_positions


def bunnies_move(bunnies_pos):
    for row, col in bunnies_pos:
        for direction in directions.values():
            new_row, new_col = row + direction[0], col + direction[1]

            if check_indices(new_row, new_col):
                matrix[new_row][new_col] = 'B'


def show_results(status='won'):
    [print(*row, sep='') for row in matrix]
    print(f"{status}: {player_row} {player_col}")

    raise SystemExit


def check_player_alive(row, col):
    if matrix[row][col] == 'B':
        show_results('dead')


rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]
commands = list(input())

won = False

directions = {
    'L': [0, -1],
    'R': [0, 1],
    'U': [-1, 0],
    'D': [1, 0],
}
player_row, player_col = find_player_position()
matrix[player_row][player_col] = '.'

for command in commands:
    new_player_row, new_player_col = player_row + directions[command][0], player_col + directions[command][1]

    if check_indices(new_player_row, new_player_col, True):
        player_row, player_col = new_player_row, new_player_col

    bunnies_move(find_bunnies_positions())

    if won:
        show_results()

    check_player_alive(player_row, player_col)




