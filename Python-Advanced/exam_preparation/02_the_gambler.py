size = int(input())

game_board = []
gambler_pos = []

total_amount = 100

lost_the_game = False

for row in range(size):
    line = list(input())
    game_board.append(line)

    if 'G' in line:
        gambler_pos = [row, line.index('G')]
        game_board[row][gambler_pos[1]] = '-'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

command = input()
while command != 'end':

    row, col = gambler_pos[0] + directions[command][0], gambler_pos[1] + directions[command][1]

    if not (0 <= row < size and 0 <= col < size):
        lost_the_game = True
        break

    gambler_pos = [row, col]
    move = game_board[row][col]
    game_board[row][col] = '-'
    if move == 'W':
        total_amount += 100
    elif move == 'P':
        total_amount -= 200
    elif move == 'J':
        total_amount += 100000
        print(f"You win the Jackpot!\nEnd of the game. Total amount: {total_amount}$")
        break

    if total_amount <= 0:
        lost_the_game = True
        break

    command = input()

else:
    print(f"End of the game. Total amount: {total_amount}$")

if lost_the_game:
    print("Game over! You lost everything!")
else:
    game_board[gambler_pos[0]][gambler_pos[1]] = 'G'
    [print(*row, sep='') for row in game_board]