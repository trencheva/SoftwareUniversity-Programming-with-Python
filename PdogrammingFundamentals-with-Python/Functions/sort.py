numbers_as_string = input().split()
numbers_as_digit = []
for number in numbers_as_string:
    numbers_as_digit.append(int(number))

sorted_numbers = sorted(numbers_as_digit)
print(sorted_numbers)