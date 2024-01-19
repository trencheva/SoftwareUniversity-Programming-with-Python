rows = int(input())

matrix = [list(input())for el in range(rows)]

searched_symbol = input()

for row_index in range(len(matrix)):
    if searched_symbol in matrix[row_index]:
        print(f'({row_index}, {matrix[row_index].index(searched_symbol)})')
        exit()

print(f'{searched_symbol} does not occur in the matrix')
