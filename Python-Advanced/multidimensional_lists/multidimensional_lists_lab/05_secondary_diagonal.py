n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(el) for el in input().split()])

diagonal_sum = 0

col_index = [el for el in range(n)]

for row_index in range(n):
    diagonal_sum += matrix[row_index][col_index.pop()]

print(diagonal_sum)