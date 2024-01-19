flatten_matrix = []

for _ in range(int(input())):

    flatten_matrix.extend([int(el) for el in input().split(', ')])

print(flatten_matrix)