n = int(input())

primary = 0
secondary = 0

for row in range(n):

    data = [int(el) for el in input().split()]
    primary += data[row]
    secondary += data[n - row - 1]

print(abs(primary - secondary))
