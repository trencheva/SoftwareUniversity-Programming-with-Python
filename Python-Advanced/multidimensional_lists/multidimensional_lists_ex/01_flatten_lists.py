line = input().split('|')

for numbers in line[::-1]:
    numbers = numbers.split()

    if numbers:
        print(*numbers, end=' ')
