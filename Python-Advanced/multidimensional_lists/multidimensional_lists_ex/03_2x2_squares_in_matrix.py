rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

count_square_matrix = 0
for row in range(rows - 1):
    for col in range(cols - 1):
        element = matrix[row][col]
        under = matrix[row + 1][col]
        right = matrix[row][col + 1]
        diagonal = matrix[row + 1][col + 1]

        if element == under and element == right and element == diagonal:
            count_square_matrix += 1

print(count_square_matrix)