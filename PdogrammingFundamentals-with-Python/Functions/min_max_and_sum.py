numbers_as_string = input().split()
numbers_as_digits = []
for number in numbers_as_string:
    numbers_as_digits.append(int(number))
minimum_number = min(numbers_as_digits)
maximum_number = max(numbers_as_digits)
sum_of_all_numbers = sum(numbers_as_digits)
print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_all_numbers}")
