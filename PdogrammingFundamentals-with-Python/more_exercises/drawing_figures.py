print('Pattern Drawing Program')

while True:
    print()
    print('Menu:')
    print('1. Draw a Triangle')
    print('2. Draw a Rectangle')
    print('3. Draw a Pyramid')
    print('4. Quit')
    print()
    print('Enter your choice (1/2/3/4):')
    command = input()

    if command == "1":
        print('Enter the number of rows for the triangle:')
        n = int(input())
        print('Enter "u" for upward or "d" for downward:')
        type_of_triangle = input()
        if type_of_triangle == "u":
            col = 1
            for r in range(n):
                for c in range(col):
                    print('*', end='')
                print()
                col += 1
        elif type_of_triangle == "d":
            for r in range(n):
                for c in range(n, 0, -1):
                    print('*', end='')
                n -= 1
                print()

    elif command == '2':
        print('Enter the number of rows for the rectangle:')
        r = int(input())
        print('Enter the number of columns for the rectangle:')
        c = int(input())
        for rows in range(r):
            for col in range(c):
                print('*', end='')
            print()

    elif command == '3':
        print('Enter the number of rows for the pyramid:')
        r = int(input())
        space = r - 1
        stars = 1
        for rows in range(r):
            for cols in range(space):
                print(' ', end='')
            space -= 1
            for s in range(stars):
                print('*', end='')
            stars += 2
            print()

    elif command == '4':
        print('Goodbye!')
        break

    else:
        print('Invalid')
        continue
