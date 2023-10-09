def is_number_perfect(number: int) -> bool:
    sum_of_numbers = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum_of_numbers += divisor
    if number == sum_of_numbers:
        return True
    return False


number_input = int(input())
if is_number_perfect(number_input):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
