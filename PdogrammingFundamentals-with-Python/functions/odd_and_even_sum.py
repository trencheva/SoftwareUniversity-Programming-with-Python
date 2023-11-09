def sum_of_all_even_and_odd_digits(number: str):
    sum_of_odd = 0
    sum_of_even = 0
    for digit in number:
        if int(digit) % 2 == 0:
            sum_of_even += int(digit)
        else:
            sum_of_odd += int(digit)
    return sum_of_odd, sum_of_even


number_input = input()
sum_of_odd_digits, sum_of_even_digits = sum_of_all_even_and_odd_digits(number_input)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
