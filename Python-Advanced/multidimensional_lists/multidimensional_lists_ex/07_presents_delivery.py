def cookie(gifts, good_kids_visited):
    for coordinates in directions.values():
        row = santa_pos[0] + coordinates[0]
        col = santa_pos[1] + coordinates[1]

        if neighborhood[row][col].isalpha():
            if neighborhood[row][col] == 'V':
                good_kids_visited += 1

            gifts -= 1
            neighborhood[row][col] = '-'

        if gifts == 0:
            break

    return gifts, good_kids_visited


number_of_presents = int(input())
size = int(input())

neighborhood = []
santa_pos = []

total_nice_kids = 0
visited_nice_kids = 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

for row in range(size):
    line = input().split()

    neighborhood.append(line)

    if 'S' in line:
        santa_pos = [row, line.index('S')]
        neighborhood[santa_pos[0]][santa_pos[1]] = '-'

    total_nice_kids += line.count('V')

command = input()

while command != 'Christmas morning':

    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1],
    ]

    house = neighborhood[santa_pos[0]][santa_pos[1]]

    if house == 'V':
        visited_nice_kids += 1
        number_of_presents -= 1

    elif house == 'C':
        number_of_presents, visited_nice_kids = cookie(number_of_presents, visited_nice_kids)

    neighborhood[santa_pos[0]][santa_pos[1]] = '-'

    if not number_of_presents or total_nice_kids == visited_nice_kids:
        break

    command = input()

neighborhood[santa_pos[0]][santa_pos[1]] = 'S'

if not number_of_presents and total_nice_kids > visited_nice_kids:
    print("Santa ran out of presents!")

[print(*row) for row in neighborhood]

if visited_nice_kids == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - visited_nice_kids} nice kid/s.")



