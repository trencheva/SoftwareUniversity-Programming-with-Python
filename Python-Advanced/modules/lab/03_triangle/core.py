def print_top(num):
    for row in range(1, num + 1):
        for n in range(1, row+1):
            print(n, end='')
        print()


def print_bottom(num):
    for row in range(num-1, 0, -1):
        for n in range(1, row+1):
            print(n, end='')
        print()


def print_triangle(num):
    print_top(num)
    print_bottom(num)

