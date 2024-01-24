def check_indices(r, c):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def cookie(matrix, gifts, good_kids_visited):
    for r, c in directions.values():

        row, col = santa_pos[0] + r, santa_pos[1] + c

        if check_indices(row, col):

            if matrix[row][col] == 'V':
                good_kids_visited += 1
                gifts -= 1
            elif matrix[row][col] == 'X':
                gifts -= 1
            matrix[row][col] = '-'

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

    if 'V' in line:
        total_nice_kids += line.count('V')


command = input()

while command != 'Christmas morning':

    row, col = santa_pos[0] + directions[command][0], santa_pos[1] + directions[command][1]

    if check_indices(row, col):

        house = neighborhood[row][col]
        santa_pos = [row, col]
        neighborhood[row][col] = '-'

        if house == 'V':
            visited_nice_kids += 1
            number_of_presents -= 1

        elif house == 'X':
            number_of_presents -= 1

        elif house == 'C':
            number_of_presents, visited_nice_kids = cookie(neighborhood, number_of_presents, visited_nice_kids)

        if number_of_presents == 0:
            print("Santa ran out of presents!")
            break

    command = input()

neighborhood[santa_pos[0]][santa_pos[1]] = 'S'
[print(*row) for row in neighborhood]
if visited_nice_kids == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - visited_nice_kids} nice kid/s.")



