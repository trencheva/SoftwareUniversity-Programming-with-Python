def calculation(operator, first_number, second_number):
    result = None
    if operator == 'multiply':
        result = first_number * second_number
    elif operator == 'divide':
        result = int(first_number / second_number)
    elif operator == 'add':
        result = first_number + second_number
    elif operator == 'subtract':
        result = first_number - second_number
    return result


input_operator = input()
first_number = int(input())
second_number = int(input())
print(calculation(input_operator, first_number, second_number))
