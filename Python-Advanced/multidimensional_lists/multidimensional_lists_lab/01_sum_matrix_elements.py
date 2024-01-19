row, cow = [int(el) for el in input().split(', ')]

sum_of_numbers = 0

matrix = []
for _ in range(row):
    sub_matrix = [int(el) for el in input().split(', ')]

    sum_of_numbers += sum(sub_matrix)
    matrix.append(sub_matrix)

print(sum_of_numbers)
print(matrix)