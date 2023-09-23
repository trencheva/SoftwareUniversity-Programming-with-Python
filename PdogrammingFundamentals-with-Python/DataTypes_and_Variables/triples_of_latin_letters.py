number = int(input())
for first_column in range(number):
    for second_column in range(number):
        for third_column in range(number):
            print(f'{chr(97 + first_column)}{chr(97 + second_column)}{chr(97 + third_column)}')
