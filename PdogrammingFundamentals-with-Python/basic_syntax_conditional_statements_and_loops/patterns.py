number = int(input())
columns = 1
for rows in range(1, number+1):
    for cols in range(1, columns + 1):
        print("*", end='')
    columns += 1
    print()

for down_rows in range(number-1, 0, -1):
    for down_cols in range(columns-2, 0, -1):
        print("*", end='')
    columns -= 1
    print()