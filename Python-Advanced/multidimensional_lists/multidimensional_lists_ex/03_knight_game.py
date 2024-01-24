def check_valid_coordinates(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True


size = int(input())

matrix = [list(input()) for _ in range(size)]

removed_knights = 0

directions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1),
)

while True:
    most_dangerous_horse_pos = []
    max_horse_attacks = 0

    for row in range(size):
        for col in range(size):

            if matrix[row][col] == 'K':
                current_horse_pos = [row, col]
                current_horse_attacks = 0

                for direction in directions:
                    r = current_horse_pos[0] + direction[0]
                    c = current_horse_pos[1] + direction[1]

                    if check_valid_coordinates(r, c):
                        if matrix[r][c] == 'K':
                            current_horse_attacks += 1

                if current_horse_attacks > max_horse_attacks:
                    max_horse_attacks = current_horse_attacks
                    most_dangerous_horse_pos = current_horse_pos

    if most_dangerous_horse_pos:
        matrix[most_dangerous_horse_pos[0]][most_dangerous_horse_pos[1]] = '0'
        removed_knights += 1
    else:
        break

print(removed_knights)


