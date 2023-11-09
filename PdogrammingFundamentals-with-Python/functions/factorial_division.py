def factorial_division(number: int) -> float:
    for current_number in range(1, number):
        number *= current_number
    return number


first_number = int(input())
second_number = int(input())
result = factorial_division(first_number) / factorial_division(second_number)
print(f'{result:.2f}')
