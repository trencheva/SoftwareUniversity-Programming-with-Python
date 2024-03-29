rows, cols = [int(el) for el in input().split()]

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

max_sum_matrix = float('-inf')
inner_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):

        first_row = matrix[row][col:col+3]
        second_row = matrix[row+1][col:col+3]
        third_row = matrix[row+2][col:col+3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if current_sum > max_sum_matrix:
            max_sum_matrix = current_sum
            inner_matrix = [first_row, second_row, third_row]

print(f'Sum = {max_sum_matrix}')
[print(*row) for row in inner_matrix]
