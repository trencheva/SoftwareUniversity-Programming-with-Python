n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(el) for el in input().split()])

diagonal_sum = 0
for index in range(n):
    diagonal_sum += matrix[index][index]

print(diagonal_sum)