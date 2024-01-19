rows, cols = [int(el) for el in input().split(', ')]

matrix = []
for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

for col_index in range(cols):
    sum_of_cols = 0
    for row_index in range(rows):
        sum_of_cols += matrix[row_index][col_index]
    print(sum_of_cols)


