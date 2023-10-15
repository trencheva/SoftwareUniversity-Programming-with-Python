numbers = [int(number) for number in input().split(', ')]

indices_of_even_numbers = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]

print(indices_of_even_numbers)