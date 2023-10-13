def top5_greater_then_the_average(numbers: list):
    numbers_as_integers = []
    greater_numbers = []
    for number in numbers:
        numbers_as_integers.append(int(number))
    average_number = sum(numbers_as_integers) / len(numbers_as_integers)
    for current_number in numbers_as_integers:
        if current_number > average_number:
            greater_numbers.append(current_number)
    greater_numbers = sorted(greater_numbers, reverse=True)
    while len(greater_numbers) > 5:
        greater_numbers.pop()
    if greater_numbers:
        print(*greater_numbers)
    else:
        print('No')


numbers_as_string = input().split()
top5_greater_then_the_average(numbers_as_string)
