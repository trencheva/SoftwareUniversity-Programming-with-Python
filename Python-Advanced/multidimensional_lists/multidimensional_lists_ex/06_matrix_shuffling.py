def indices_validator(ind):
    if 0 <= ind[0] <= rows and 0 <= ind[2] <= rows and 0 <= ind[1] <= cols and 0 <= ind[3] <= cols:
        return True
    return False


def swap_command(command, indices):
    if command == 'swap' and len(indices) == 4 and indices_validator(indices):
        matrix[indices[0]][indices[1]], matrix[indices[2]][indices[3]] = matrix[indices[2]][indices[3]], matrix[indices[0]][indices[1]]
        [print(*row) for row in matrix]
    else:
        print('Invalid input!')


rows, cols = [int(x) for x in input().split()]

matrix = [[int(el) for el in input().split()] for _ in range(rows)]


while True:
    command, *indices = [int(el) if el.isdigit() else el for el in input().split()]

    if command == 'END':
        break

    swap_command(command, indices)